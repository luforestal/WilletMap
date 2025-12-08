"""
Helper script to convert Boundaries.shp to GeoJSON
"""

import geopandas as gpd
import json
from pathlib import Path

def convert_shapefile_to_geojson():
    """Convert shapefile to GeoJSON for use in MapLibre"""
    
    shapefile_path = Path("Boundaries.shp")
    
    if not shapefile_path.exists():
        print(f"❌ Error: {shapefile_path} not found")
        return
    
    # Read shapefile
    gdf = gpd.read_file(shapefile_path)
    
    # Ensure CRS is set
    if gdf.crs is None:
        print("⚠️  No CRS found, assuming EPSG:3310")
        gdf = gdf.set_crs(epsg=3310)
    
    # Convert to WGS84 (required for web maps)
    gdf = gdf.to_crs(epsg=4326)
    
    # Convert to GeoJSON
    geojson = json.loads(gdf.to_json())
    
    # Create JavaScript module content
    js_content = f"""// School boundary data - Auto-generated from shapefile
// Original CRS: {gdf.crs}

export const boundaryData = {json.dumps(geojson, indent=2)}
"""
    
    # Write to file
    output_path = Path("src/data/boundary.js")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w") as f:
        f.write(js_content)
    
    print(f"✅ Successfully generated {output_path}")
    print(f"   Features: {len(geojson['features'])}")
    print(f"   Geometry type: {geojson['features'][0]['geometry']['type'] if geojson['features'] else 'None'}")

if __name__ == "__main__":
    convert_shapefile_to_geojson()
