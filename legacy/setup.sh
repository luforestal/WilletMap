#!/bin/bash

# Willet Tree Map - Quick Setup Script
# This script helps you set up the React app quickly

set -e

echo "🌳 Willet Tree Map - React Setup"
echo "================================"
echo ""

# Check if Excel file exists
if [ ! -f "WilletTreeInventory_coordinates.xlsx" ]; then
    echo "❌ Error: WilletTreeInventory_coordinates.xlsx not found"
    echo "   Please make sure the Excel file is in the current directory"
    exit 1
fi

# Check if Boundaries.shp exists
if [ ! -f "Boundaries.shp" ]; then
    echo "⚠️  Warning: Boundaries.shp not found"
    echo "   Boundary layer will not be available"
    SKIP_BOUNDARY=true
else
    SKIP_BOUNDARY=false
fi

# Step 1: Convert data
echo "📊 Step 1: Converting Excel data..."
python convert_data.py

if [ "$SKIP_BOUNDARY" = false ]; then
    echo "🗺️  Converting boundary shapefile..."
    python convert_boundary.py
fi

# Step 2: Update photo URLs
echo ""
echo "📸 Step 2: Updating photo URLs..."
read -p "Enter your GitHub username: " GITHUB_USER
read -p "Enter your repository name (default: WilletMap): " GITHUB_REPO
GITHUB_REPO=${GITHUB_REPO:-WilletMap}

if [ -f "src/data/trees.js" ]; then
    sed -i "s/USERNAME/$GITHUB_USER/g" src/data/trees.js
    sed -i "s/REPO/$GITHUB_REPO/g" src/data/trees.js
    echo "✅ Updated photo URLs with: $GITHUB_USER/$GITHUB_REPO"
fi

# Step 3: Install dependencies
echo ""
echo "📦 Step 3: Installing dependencies..."
if ! command -v npm &> /dev/null; then
    echo "❌ Error: npm is not installed"
    echo "   Please install Node.js from https://nodejs.org/"
    exit 1
fi

npm install

# Step 4: Check if photos need to be committed
echo ""
if [ -d "Photos" ]; then
    echo "📸 Photos directory found"
    read -p "Do you want to commit and push photos to GitHub? (y/n): " PUSH_PHOTOS
    if [ "$PUSH_PHOTOS" = "y" ]; then
        git add Photos/
        git commit -m "Add tree photos" || echo "Photos already committed"
        git push || echo "Please push manually with: git push"
    fi
else
    echo "⚠️  Warning: Photos directory not found"
    echo "   You'll need to add photos manually"
fi

# Done!
echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 Next steps:"
echo "   1. Start dev server: npm run dev"
echo "   2. Open your browser to the URL shown"
echo "   3. Verify the map displays correctly"
echo "   4. Build for production: npm run build"
echo ""
echo "📚 For more info, see GETTING_STARTED.md"
