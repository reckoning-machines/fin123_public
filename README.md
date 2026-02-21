# fin123 GitHub Pages site

This folder contains a static site (HTML/CSS, optional JS) intended to be served by GitHub Pages.

## Files

- `index.html`
- `styles.css`
- `script.js` (optional)

## Deploy on GitHub Pages

### Option A: Deploy from the repository root
1. Put `index.html`, `styles.css`, and `script.js` in the repo root.
2. In GitHub:
   - Go to **Settings** → **Pages**
   - Under **Build and deployment**
     - **Source**: Deploy from a branch
     - **Branch**: `main` (or `master`)
     - **Folder**: `/ (root)`
3. Save. GitHub Pages will publish the site.

### Option B: Deploy from `/docs`
1. Create a `docs/` directory in the repo.
2. Put `index.html`, `styles.css`, and `script.js` inside `docs/`.
3. In GitHub:
   - **Settings** → **Pages**
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/docs`
4. Save.

## Update the "Download" button later

In `index.html`, find the disabled button:

```html
<button class="btn btn-disabled" type="button" disabled aria-disabled="true">
  Download (coming soon)
</button>