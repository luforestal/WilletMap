# Sidebar vs Popup Feature

## Overview

The tree map now supports **two display modes** for tree information:

### 🎯 Sidebar Mode (Default)
- Click on any tree marker to open a **right sidebar** with full details
- Sidebar shows:
  - Tree code, genus, species
  - DBH, height, crown size
  - GPS coordinates
  - **Large photo** (when available)
- Map automatically flies to the selected tree
- Clean, organized layout

### 💬 Popup Mode (Alternative)
- Click on any tree marker to see a **small popup**
- Popup shows same info in compact format
- Traditional Leaflet/Folium style
- Smaller photo inline

## How to Switch

Use the toggle buttons in the top-left control panel:
- **📋 Sidebar** - Shows info in right panel (recommended)
- **💬 Popup** - Shows info in small popups

## Features

### Sidebar Benefits
✅ More space for content  
✅ Larger photos  
✅ Better readability  
✅ Doesn't obscure map  
✅ Smooth animation  
✅ Easy to close (X button or click another tree)  

### Popup Benefits
✅ Compact and minimal  
✅ Familiar interface  
✅ Good for quick glances  
✅ Multiple popups possible  

## Technical Details

**Implementation:**
- `useSidebar` state controls mode
- Markers have click handlers in sidebar mode
- Popups attached only in popup mode
- Map flies to tree location in sidebar mode

**Responsive:**
- Sidebar adapts to screen size
- Maximum width 380px
- Full width on mobile (up to 380px)

## Try It Out

1. Visit http://localhost:5174
2. Click any tree marker (sidebar opens by default)
3. Click "💬 Popup" button to switch modes
4. Click trees again to see popup style
5. Switch back to "📋 Sidebar" for full details

## Which Should You Use?

**Use Sidebar if:**
- You want to showcase photos prominently
- Users need to see detailed information
- Professional presentation matters
- You want modern UI/UX

**Use Popup if:**
- You prefer traditional map interfaces
- Screen real estate is limited
- Quick information glance is sufficient
- You want simpler interactions

---

**Default: Sidebar mode** (can be changed in TreeMap.jsx line 15)
