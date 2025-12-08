# Willet Tree Map - React Edition

A modern, interactive tree inventory map built with React and MapLibre GL JS, replacing the original Python/Folium implementation.

## 🚀 Quick Start

### Prerequisites
- Node.js (v16 or higher)
- npm or yarn

### Installation

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

## 📋 Data Setup

### 1. Prepare Your Tree Data

Edit `src/data/trees.js` with your actual tree inventory data from the Excel file. For each tree, you need:

- `treeCode`: Unique identifier
- `lat`, `lon`: GPS coordinates
- `genus`, `species`: Taxonomic information
- `dbh`: Diameter at breast height (cm)
- `height`: Tree height (m)
- `crownNS`, `crownEW`: Canopy dimensions (meters)
- `photoUrl`: Direct link to the tree photo on GitHub

### 2. Upload Photos to GitHub

Instead of embedding photos in the app, upload them to your GitHub repository:

```bash
# Create a Photos directory (if not already exists)
mkdir -p Photos

# Add photos
git add Photos/
git commit -m "Add tree photos"
git push
```

Then use the raw GitHub URLs in your tree data:
```
https://raw.githubusercontent.com/USERNAME/REPO/main/Photos/PHOTO.jpg
```

### 3. Convert Boundary Shapefile

Convert your `Boundaries.shp` to GeoJSON format:

**Option 1: Using ogr2ogr (recommended)**
```bash
ogr2ogr -f GeoJSON src/data/boundary.json Boundaries.shp
```

**Option 2: Using Node.js tool**
```bash
npx -y shp2json Boundaries.shp -o src/data/boundary.json
```

Then update `src/data/boundary.js` to import the JSON file.

## 🗺️ Features

- **Multiple Base Maps**: Switch between OpenStreetMap, CartoDB, and Satellite imagery
- **Interactive Markers**: Color-coded by genus with different shapes
- **Tree Canopies**: Visual representation of crown spread
- **Popups**: Detailed tree information with photos
- **School Boundary**: Overlay showing property limits
- **Responsive**: Works on desktop and mobile devices

## 🎨 Customization

### Colors and Shapes

Edit the `colors` and `shapes` objects in `src/data/trees.js` to customize how different genera appear on the map.

### Styling

- Map controls: `src/components/TreeMap.css`
- Global styles: `src/index.css`

## 📦 Project Structure

```
WilletMap/
├── src/
│   ├── components/
│   │   ├── TreeMap.jsx       # Main map component
│   │   └── TreeMap.css        # Map styles
│   ├── data/
│   │   ├── trees.js           # Tree inventory data
│   │   └── boundary.js        # School boundary GeoJSON
│   ├── App.jsx                # Root component
│   ├── main.jsx               # Entry point
│   └── index.css              # Global styles
├── public/                    # Static assets
├── index.html                 # HTML template
├── package.json               # Dependencies
└── vite.config.js             # Vite configuration
```

## 🔧 Development Tips

### Testing with Sample Data

The app includes example data to help you get started. Replace it with your actual tree inventory data once ready.

### Photo Management

- Use consistent naming: `t001.jpg`, `t002.jpg`, etc.
- Optimize images before uploading (recommended max width: 800px)
- Supported formats: JPG, PNG

### Deployment

Build and deploy to GitHub Pages, Netlify, Vercel, or any static hosting:

```bash
npm run build
# The dist/ folder contains your production-ready app
```

## 🆚 Differences from Python Version

| Feature | Python (Folium) | React (MapLibre) |
|---------|----------------|------------------|
| Photos | Base64 embedded | GitHub URLs |
| Performance | Slower with many trees | Fast, hardware-accelerated |
| Deployment | Single HTML file | Modern web app |
| Customization | Limited | Fully customizable |
| Mobile | Basic | Optimized |

## 📝 License

Same as original project.

## 🤝 Contributing

1. Update tree data in `src/data/trees.js`
2. Add photos to GitHub repo
3. Test locally with `npm run dev`
4. Build and deploy with `npm run build`

---

**Note**: Make sure to update the photo URLs and boundary data with your actual files before deploying!
