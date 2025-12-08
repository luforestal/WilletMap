# ⚡ Quick Start (2 minutes)

## If you just want to see it working:

```bash
# 1. Run the automated setup
./setup.sh

# 2. Start the dev server
npm run dev

# 3. Open your browser to the URL shown (usually http://localhost:5173)
```

That's it! 🎉

---

## Manual Setup (if setup.sh doesn't work):

```bash
# 1. Convert your data
python convert_data.py
python convert_boundary.py

# 2. Update GitHub URLs in src/data/trees.js
# Replace 'USERNAME/REPO' with your actual GitHub username and repo name

# 3. Install and run
npm install
npm run dev
```

---

## To Deploy:

```bash
npm run build

# Then push the dist/ folder to your hosting provider
# Or use: git subtree push --prefix dist origin gh-pages
```

---

## Need detailed instructions?
👉 See `GETTING_STARTED.md`

## Want to understand the structure?
👉 See `PROJECT_STRUCTURE.md`

## Curious about the changes?
👉 See `COMPARISON.md`
