# 📦 Project Structure

```
WilletMap/
│
├── 🌳 ORIGINAL PYTHON PROJECT
│   ├── make_tree_map.py              # Original Python/Folium implementation
│   ├── WilletTreeInventory_coordinates.xlsx  # Tree data
│   ├── Boundaries.shp                # School boundary (+ .dbf, .shx, etc.)
│   └── Photos/                       # Tree photos (auto-downloaded)
│
├── ⚛️ NEW REACT PROJECT
│   ├── src/
│   │   ├── components/
│   │   │   ├── TreeMap.jsx          # Main map component
│   │   │   └── TreeMap.css          # Map styling
│   │   ├── data/
│   │   │   ├── trees.js             # Tree inventory (generated)
│   │   │   └── boundary.js          # Boundary GeoJSON (generated)
│   │   ├── App.jsx                  # Root component
│   │   ├── main.jsx                 # Entry point
│   │   └── index.css                # Global styles
│   │
│   ├── public/                      # Static assets
│   ├── index.html                   # HTML template
│   ├── package.json                 # Dependencies
│   └── vite.config.js               # Build config
│
├── 🛠️ HELPER SCRIPTS
│   ├── convert_data.py              # Excel → JavaScript converter
│   ├── convert_boundary.py          # Shapefile → GeoJSON converter
│   └── setup.sh                     # Automated setup script
│
└── 📚 DOCUMENTATION
    ├── README.md                    # Original README
    ├── README_REACT.md              # React app documentation
    ├── GETTING_STARTED.md           # Step-by-step guide
    └── COMPARISON.md                # Python vs React comparison
```

## Quick Reference

### 🚀 First Time Setup
```bash
./setup.sh
```

### 🔄 Update Data
```bash
python convert_data.py
npm run dev
```

### 📸 Add Photos
```bash
git add Photos/
git commit -m "Add photos"
git push
```

### 🏗️ Build for Production
```bash
npm run build
```

### 🌐 Deploy
```bash
# GitHub Pages
npm run build && git subtree push --prefix dist origin gh-pages

# Or use Netlify/Vercel (automatic)
```

## Files You'll Edit

### Regularly
- `src/data/trees.js` - Tree inventory data
- `src/data/boundary.js` - Boundary coordinates

### Occasionally  
- `src/components/TreeMap.css` - Styling
- `src/components/TreeMap.jsx` - Map logic

### Rarely
- `package.json` - Dependencies
- `vite.config.js` - Build settings

## Files Generated Automatically

- `node_modules/` - Dependencies (don't commit)
- `dist/` - Production build (don't commit)
- `src/data/trees.js` - From convert_data.py
- `src/data/boundary.js` - From convert_boundary.py

## Git Management

### What to Commit
```bash
git add src/
git add Photos/
git add package.json
git add index.html
git add vite.config.js
git add *.md
```

### What NOT to Commit
```bash
# Already in .gitignore
node_modules/
dist/
*.log
```

## Development Workflow

1. **Make changes** to data or code
2. **Test locally** with `npm run dev`
3. **Build** with `npm run build`
4. **Deploy** (push to GitHub or hosting platform)

## Common Commands

```bash
# Install dependencies
npm install

# Start dev server (with hot reload)
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Convert Excel to JavaScript
python convert_data.py

# Convert shapefile to GeoJSON
python convert_boundary.py

# Run complete setup
./setup.sh
```

## Environment Variables (Optional)

Create a `.env` file if needed:
```
VITE_GITHUB_USER=yourusername
VITE_GITHUB_REPO=WilletMap
```

Then use in code:
```javascript
const photoUrl = `https://raw.githubusercontent.com/${import.meta.env.VITE_GITHUB_USER}/${import.meta.env.VITE_GITHUB_REPO}/main/Photos/${photo}.jpg`
```

## Troubleshooting Quick Fixes

### Map not loading
```bash
rm -rf node_modules package-lock.json
npm install
```

### Photos not showing
- Check GitHub URLs are correct
- Verify photos are pushed to GitHub
- Check browser console (F12)

### Build errors
```bash
npm run build -- --debug
```

### Port already in use
```bash
npm run dev -- --port 3000
```

## Next Steps

1. ✅ Run `./setup.sh` to set everything up
2. ✅ Visit http://localhost:5173 to see your map
3. ✅ Customize colors/styles in `src/data/trees.js`
4. ✅ Deploy to GitHub Pages or Netlify

## Need Help?

- 📖 Read `GETTING_STARTED.md` for detailed instructions
- 🔍 Check `README_REACT.md` for feature documentation
- 📊 See `COMPARISON.md` to understand differences from Python version

---

**Happy mapping! 🗺️**
