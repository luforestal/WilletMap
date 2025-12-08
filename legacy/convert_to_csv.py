"""
Convert Excel tree inventory to CSV format
This allows the React app to load data dynamically without hardcoding
"""

import pandas as pd
from pathlib import Path

# Configuration
DATA_FILE = "/home/dguerrero/Downloads/Cooley_Ranch/Cooley_Ranch_Tree Data_coordinates.xlsx"
SHEET_NAME = 1
OUTPUT_CSV = "public/tree_data.csv"

def convert_to_csv():
    """Convert Excel to CSV with all necessary columns"""
    
    # Read Excel file
    df = pd.read_excel(DATA_FILE, sheet_name=SHEET_NAME)
    
    # Keep only rows with coordinates
    df_map = df.dropna(subset=["lat", "lon"]).copy()
    
    # Select and rename columns for web app
    columns_to_keep = {
        "TreeCode": "treeCode",
        "lat": "lat",
        "lon": "lon",
        "Genus": "genus",
        "Species": "species",
        "DBH1cm": "dbh",
        "Heightm": "height",
        "CrownNSm": "crownNS",
        "CrownEWm": "crownEW"
    }
    
    # Create output dataframe
    output_df = pd.DataFrame()
    for old_col, new_col in columns_to_keep.items():
        if old_col in df_map.columns:
            output_df[new_col] = df_map[old_col]
        else:
            print(f"⚠️  Warning: Column '{old_col}' not found in Excel file")
    
    # Clean up data
    output_df = output_df.fillna('')
    
    # Create output directory if needed
    output_path = Path(OUTPUT_CSV)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Save to CSV
    output_df.to_csv(output_path, index=False)
    
    print(f"✅ Successfully converted to CSV")
    print(f"   Input:  {DATA_FILE}")
    print(f"   Output: {OUTPUT_CSV}")
    print(f"   Trees:  {len(output_df)}")
    print()
    print("📝 Columns included:")
    for col in output_df.columns:
        print(f"   - {col}")

if __name__ == "__main__":
    convert_to_csv()
