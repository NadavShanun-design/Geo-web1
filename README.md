# GeoDo Website

## Local Development

### Option 1: Use the included Python server (Recommended)
```bash
python3 server.py
```
Then visit: http://localhost:8000

This server automatically sends no-cache headers to prevent browser caching.

### Option 2: Use Python's built-in server
```bash
python3 -m http.server 8000
```
Then visit: http://localhost:8000

**Important:** After making changes, do a hard refresh:
- **Mac:** `Cmd + Shift + R`
- **Windows/Linux:** `Ctrl + Shift + R`

### Option 3: Use Node.js http-server
```bash
npx http-server -p 8000 -c-1
```
The `-c-1` flag disables caching.

## Cache Issues?

If you see old content in your browser:

1. **Hard Refresh:**
   - Mac: `Cmd + Shift + R`
   - Windows: `Ctrl + Shift + R`

2. **Clear Browser Cache:**
   - Chrome: Settings → Privacy → Clear browsing data
   - Firefox: Settings → Privacy → Clear Data

3. **Use Incognito/Private Window:**
   - This bypasses cache completely

4. **Add `?nocache=1` to URL:**
   - Visit: http://localhost:8000?nocache=1

## Deployment

This site is deployed to Vercel and GitHub Pages.

Repository: https://github.com/NadavShanun-design/Geo-web1
