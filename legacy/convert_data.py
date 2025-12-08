"""
Helper script to convert Excel tree inventory to JavaScript format
Run this to generate the trees.js data file from your Excel file
"""

import pandas as pd
import json
from pathlib import Path

# Configuration - match your original script
DATA_FILE = "WilletTreeInventory_coordinates.xlsx"
SHEET_NAME = 1

# Color palette for genera
COLORS = [
    "red", "blue", "green", "purple", "orange",
    "darkred", "darkblue", "darkgreen", "cadetblue",
    "pink", "black", "gray"
]

# Shape specifications
SHAPES = [
    {"sides": 3, "rotation": 0},
    {"sides": 4, "rotation": 45},
    {"sides": 5, "rotation": 0},
    {"sides": 6, "rotation": 0},
    {"sides": 8, "rotation": 0},
    {"sides": 3, "rotation": 180},
    {"sides": 4, "rotation": 0}
]

def convert_excel_to_js():
    """Convert Excel data to JavaScript module format"""
    
    # Read Excel file
    df = pd.read_excel(DATA_FILE, sheet_name=SHEET_NAME)
    df_map = df.dropna(subset=["lat", "lon"]).copy()
    
    # Get unique genera
    genera = sorted(df_map["Genus"].dropna().unique())
    
    # Create genus-to-color mapping
    genus_colors = {}
    genus_shapes = {}
    for i, genus in enumerate(genera):
        genus_colors[genus] = COLORS[i % len(COLORS)]
        genus_shapes[genus] = SHAPES[i % len(SHAPES)]
    
    # Build tree data
    trees = []
    for _, row in df_map.iterrows():
        tree_code = str(row.get("TreeCode", "")).strip()
        genus = row.get("Genus", "NA")
        
        # Calculate crown radius
        crown_ns = row.get("CrownNSm", None)
        crown_ew = row.get("CrownEWm", None)
        
        tree = {
            "treeCode": tree_code,
            "lat": float(row["lat"]),
            "lon": float(row["lon"]),
            "genus": genus,
            "species": row.get("Species", ""),
            "dbh": row.get("DBH1cm", None),
            "height": row.get("Heightm", None),
            "crownNS": crown_ns if pd.notna(crown_ns) else None,
            "crownEW": crown_ew if pd.notna(crown_ew) else None,
            "color": genus_colors.get(genus, "gray"),
            "shape": genus_shapes.get(genus, {"sides": 4, "rotation": 0}),
            "photoUrl": f"https://raw.githubusercontent.com/USERNAME/REPO/main/Photos/{tree_code.lower()}.jpg"
        }
        
        trees.append(tree)
    
    # Generate JavaScript file content
    js_content = f"""// Tree inventory data - Auto-generated from Excel
// Generated from: {DATA_FILE}

// Color palette for different genera
const colors = {json.dumps(genus_colors, indent=2).replace('true', 'true').replace('false', 'false')}

// Shape configurations for different genera
const shapes = {json.dumps(genus_shapes, indent=2)}

// Tree data
export const treeData = {json.dumps(trees, indent=2)}

// Calculate crown radius for each tree (converts meters to approximate pixels at zoom level 18)
// Rough conversion: 1 meter ≈ 5 pixels at zoom 18
treeData.forEach(tree => {{
  if (tree.crownNS && tree.crownEW) {{
    tree.crownRadius = ((tree.crownNS + tree.crownEW) / 4) * 5
  }} else if (tree.crownNS) {{
    tree.crownRadius = (tree.crownNS / 2) * 5
  }} else if (tree.crownEW) {{
    tree.crownRadius = (tree.crownEW / 2) * 5
  }}
}})
"""
    
    # Write to file
    output_path = Path("src/data/trees.js")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w") as f:
        f.write(js_content)
    
    print(f"✅ Successfully generated {output_path}")
    print(f"   Total trees: {len(trees)}")
    print(f"   Unique genera: {len(genera)}")
    print()
    print("📝 Next steps:")
    print("   1. Upload photos to your GitHub repo in a 'Photos' folder")
    print("   2. Update photoUrl in trees.js with your actual GitHub username/repo")
    print("   3. Run: npm install")
    print("   4. Run: npm run dev")

if __name__ == "__main__":
    convert_excel_to_js()
