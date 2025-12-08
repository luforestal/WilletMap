# 🚀 Getting Started Guide

## Step-by-Step Setup

### 1. Convert Your Data

First, let's convert your Excel file and shapefile to JavaScript format:

```bash
# Convert tree inventory from Excel
python convert_data.py

# Convert boundary shapefile to GeoJSON
python convert_boundary.py
```

This will generate:
- `src/data/trees.js` - Your tree inventory
- `src/data/boundary.js` - School boundary

### 2. Prepare Photos for GitHub

Since we're not embedding photos as base64 anymore, you'll upload them to GitHub and use direct URLs:

```bash
# Photos should already be in the Photos/ directory from your original setup
# Check if they exist:
ls Photos/

# Add them to git (if not already tracked)
git add Photos/
git commit -m "Add tree photos"
git push
```

### 3. Update Photo URLs

After pushing to GitHub, update the photo URLs in `src/data/trees.js`:

Replace `USERNAME/REPO` with your actual GitHub username and repository name:
```javascript
"photoUrl": "https://raw.githubusercontent.com/USERNAME/REPO/main/Photos/t001.jpg"
```

You can do this automatically with:
```bash
# Replace USERNAME and REPO with your values
sed -i 's/USERNAME/luforestal/g' src/data/trees.js
sed -i 's/REPO/WilletMap/g' src/data/trees.js
```

### 4. Install Dependencies

```bash
npm install
```

### 5. Run Development Server

```bash
npm run dev
```

Visit the URL shown (usually http://localhost:5173)

### 6. Build for Production

When ready to deploy:

```bash
npm run build
```

The `dist/` folder will contain your production-ready app.

## 📸 Photo Management Tips

### Option 1: Use GitHub Raw URLs (Recommended for small repos)
```
https://raw.githubusercontent.com/username/repo/main/Photos/photo.jpg
```

### Option 2: Use GitHub Pages (Better for many photos)
1. Enable GitHub Pages in your repo settings
2. Use URLs like: `https://username.github.io/repo/Photos/photo.jpg`

### Option 3: Use a CDN (Best performance)
Upload photos to a CDN like Cloudinary, Imgur, or AWS S3.

## 🗺️ Customization Guide

### Change Map Center/Zoom
Edit `src/components/TreeMap.jsx`:
```javascript
zoom: 18,  // Increase for more zoom
center: [lon, lat]  // Or set manually
```

### Add More Base Maps
In `TreeMap.jsx`, add a new case to the `changeBaseMap` function:
```javascript
case 'terrain':
  styleConfig.sources['terrain'] = {
    type: 'raster',
    tiles: ['https://tile.url/{z}/{x}/{y}.png'],
    tileSize: 256
  }
```

### Customize Marker Colors
Edit the `colors` object in `src/data/trees.js`

### Change Marker Shapes
Edit the `shapes` object in `src/data/trees.js`

## 🐛 Troubleshooting

### Photos Not Showing
- Check that photo URLs are correct and accessible
- Open browser DevTools (F12) and check Console for errors
- Verify photos are pushed to GitHub

### Map Not Loading
- Check browser console for errors
- Verify maplibre-gl is installed: `npm list maplibre-gl`
- Try clearing browser cache

### Boundary Not Appearing
- Verify boundary.js has valid GeoJSON
- Check that coordinates are in the right format (lon, lat)
- Make sure CRS is WGS84 (EPSG:4326)

## 📦 Deployment Options

### GitHub Pages
```bash
npm run build
git add dist -f
git commit -m "Deploy to GitHub Pages"
git subtree push --prefix dist origin gh-pages
```

### Netlify
1. Push your repo to GitHub
2. Connect to Netlify
3. Build command: `npm run build`
4. Publish directory: `dist`

### Vercel
```bash
npm install -g vercel
vercel
```

## 🔄 Updating Data

When your tree inventory changes:

1. Update the Excel file
2. Run `python convert_data.py`
3. Add any new photos to GitHub
4. Rebuild: `npm run build`
5. Deploy

## 💡 Tips

- Keep photos under 500KB each for faster loading
- Use JPG for photos (better compression than PNG)
- Name photos consistently: `t001.jpg`, `t002.jpg`, etc.
- Test on mobile devices (use `npm run dev -- --host` to access from phone)
- Use browser DevTools to debug issues

## 📚 Additional Resources

- [MapLibre GL JS Docs](https://maplibre.org/maplibre-gl-js/docs/)
- [React Documentation](https://react.dev/)
- [Vite Guide](https://vitejs.dev/guide/)

---

Need help? Check the README_REACT.md for more details!
