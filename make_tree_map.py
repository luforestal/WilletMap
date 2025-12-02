import pandas as pd
import folium
import numpy as np
from itertools import cycle
from pathlib import Path
import geopandas as gpd

# =====================================================
# CONFIG
# =====================================================

DATA_FILE = "WilletTreeInventory_coordinates.xlsx"
SHEET_NAME = 1
OUTPUT_HTML = "willet_tree_map.html"

# =====================================================
# MAIN FUNCTION
# =====================================================

def build_tree_map(data_path, boundary_shp="Shapes/Boundaries.shp"):
    """
    Creates a folium tree map with canopy circles, polygon markers by genus,
    and school boundary overlay from a shapefile.

    Parameters
    ----------
    data_path : str or Path
        Path to the Excel inventory file.
    boundary_shp : str
        Path to boundary shapefile relative to this .py file.

    Returns
    -------
    folium.Map
    """

    # ==========================
    # PATHS
    # ==========================
    base_dir = Path(__file__).parent
    data_path = Path(data_path)
    boundary_path = base_dir / boundary_shp

    # ==========================
    # LOAD INVENTORY
    # ==========================
    df = pd.read_excel(data_path, sheet_name=SHEET_NAME)
    df_map = df.dropna(subset=["lat", "lon"]).copy()

    center = [
        df_map["lat"].mean(),
        df_map["lon"].mean()
    ]

    # ==========================
    # BASE MAP
    # ==========================
    m = folium.Map(
        location=center,
        zoom_start=18,
        tiles="OpenStreetMap",
        name="OSM"
    )

    folium.TileLayer(
        tiles="CartoDB positron",
        name="CartoDB positron"
    ).add_to(m)

    folium.TileLayer(
        tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{x}/{y}",
        attr="Esri World Imagery",
        name="Esri Satellite",
        overlay=False,
        control=True
    ).add_to(m)

    # ==========================
    # BOUNDARY SHAPEFILE
    # ==========================
    if boundary_path.exists():

        gdf = gpd.read_file(boundary_path)

        # Fix missing CRS
        if gdf.crs is None:
            gdf = gdf.set_crs(epsg=3310, inplace=False)

        # Reproject for Folium (WGS84)
        gdf = gdf.to_crs(epsg=4326)

        folium.GeoJson(
            gdf,
            name="School boundary",
            style_function=lambda x: {
                "color": "black",
                "weight": 1,
                "fillColor": "none",
                "fillOpacity": 0
            }
        ).add_to(m)

    else:
        print(f"⚠ WARNING: boundary shapefile not found -> {boundary_path}")

    # ==========================
    # GENUS STYLES
    # ==========================
    genera = sorted(df_map["Genus"].dropna().unique())

    shape_specs = [
        {"sides": 3, "rotation": 0},
        {"sides": 4, "rotation": 45},
        {"sides": 5, "rotation": 0},
        {"sides": 6, "rotation": 0},
        {"sides": 8, "rotation": 0},
        {"sides": 3, "rotation": 180},
        {"sides": 4, "rotation": 0},
    ]

    colors = [
        "red", "blue", "green", "purple", "orange",
        "darkred", "darkblue", "darkgreen", "cadetblue",
        "pink", "black", "gray"
    ]

    shape_cycle = cycle(shape_specs)
    color_cycle = cycle(colors)

    genus_styles = {
        g: {
            "shape": next(shape_cycle),
            "color": next(color_cycle)
        }
        for g in genera
    }

    # ==========================
    # ADD TREES
    # ==========================
    for _, r in df_map.iterrows():

        lat, lon = float(r["lat"]), float(r["lon"])
        genus = r.get("Genus", "NA")
        style = genus_styles.get(genus)

        # ----- CANOPY SCALING -----
        ns = r.get("CrownNSm", np.nan)
        ew = r.get("CrownEWm", np.nan)

        crown_radius = None

        if pd.notna(ns) and pd.notna(ew):
            crown_radius = (ns + ew) / 4
        elif pd.notna(ns):
            crown_radius = ns / 2
        elif pd.notna(ew):
            crown_radius = ew / 2

        if crown_radius:
            folium.Circle(
                location=[lat, lon],
                radius=crown_radius,
                fill=True,
                fill_opacity=0.3,
                color=None,
                stroke=False
            ).add_to(m)

        # ----- POPUP -----
        popup_html = f"""
        <div style="font-size:13px;">
            <b>Tree code:</b> {r.get('TreeCode','')}<br>
            <b>Genus:</b> {r.get('Genus','')}<br>
            <b>Species:</b> {r.get('Species','')}<br>
            <b>DBH (cm):</b> {r.get('DBH1cm','')}<br>
            <b>Height (m):</b> {r.get('Heightm','')}
        </div>
        """

        popup = folium.Popup(popup_html, max_width=300)

        # ----- MARKER STYLE -----
        if style:
            shape = style["shape"]
            color = style["color"]
        else:
            shape = {"sides": 4, "rotation": 0}
            color = "gray"

        folium.RegularPolygonMarker(
            location=[lat, lon],
            number_of_sides=shape["sides"],
            rotation=shape["rotation"],
            radius=7,
            color=color,
            fill=True,
            fill_opacity=0.9,
            popup=popup
        ).add_to(m)

    # ==========================
    # CONTROLS + SAVE
    # ==========================
    folium.LayerControl().add_to(m)

    m.save(base_dir / OUTPUT_HTML)

    return m
