# 🚀 Updated Workflow - Dynamic CSV Loading

## New Approach Benefits

✅ **No hardcoding** - Tree data loaded dynamically from CSV  
✅ **Easy updates** - Just export Excel to CSV and refresh  
✅ **Smaller bundle** - Data not compiled into app  
✅ **Flexible** - Change data without rebuilding  

## Quick Workflow

### 1. Update Tree Inventory

Edit your Excel file as needed.

### 2. Convert to CSV

```bash
python convert_to_csv.py
```

This creates `public/tree_data.csv` from your Excel file.

### 3. Upload Photos

After optimizing photos (already done - 19MB total):

```bash
git add Photos/
git commit -m "Add optimized tree photos"
git push
```

### 4. Deploy

```bash
# Development
npm run dev

# Production
npm run build
git add public/ dist/
git commit -m "Update tree data"
git push
```

## File Structure

```
WilletMap/
├── WilletTreeInventory_coordinates.xlsx  ← Your source data
├── public/
│   └── tree_data.csv                     ← Auto-generated CSV
├── Photos/                                ← Optimized photos (19MB)
│   ├── a01.jpg
│   ├── a02.jpg
│   └── ...
└── src/
    ├── utils/
    │   └── treeDataLoader.js             ← CSV parser
    └── components/
        └── TreeMap.jsx                    ← Loads CSV dynamically
```

## Photo Naming Convention

The app automatically constructs photo URLs from tree codes:
- Tree code: `A01` → Photo: `Photos/a01.jpg`
- Tree code: `B15` → Photo: `Photos/b15.jpg`

Make sure photo filenames match tree codes (case-insensitive).

## GitHub Configuration

Update the GitHub config in `src/components/TreeMap.jsx` if needed:

```javascript
const { trees } = await loadTreeData('/tree_data.csv', {
  username: 'luforestal',  // Your GitHub username
  repo: 'WilletMap',       // Your repo name
  branch: 'main'           // Branch with photos
})
```

## Complete Update Process

```bash
# 1. Edit Excel file (add/remove/update trees)

# 2. Convert to CSV
python convert_to_csv.py

# 3. Test locally
npm run dev

# 4. Build and deploy
npm run build

# 5. Commit changes
git add public/tree_data.csv
git commit -m "Update tree inventory"
git push
```

## Optimization Script

Photos are already optimized (345MB → 19MB). To re-optimize:

```bash
python optimize_photos.py /path/to/original/photos Photos/ -w 800 -q 85
```

Options:
- `-w` / `--width`: Max width in pixels (default: 800)
- `-q` / `--quality`: JPEG quality 1-100 (default: 85)

## No More Hardcoding! 🎉

The old workflow required:
1. Edit Excel
2. Run `convert_data.py` to generate JavaScript
3. Rebuild entire app
4. Deploy

New workflow:
1. Edit Excel
2. Run `convert_to_csv.py` to update CSV
3. Refresh browser (dev) or rebuild (prod)

Much simpler and more maintainable!
