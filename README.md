# Energy Photonics Lab website

This repository is published as a GitHub project site:

`https://alokghanekar.github.io/Energy-Photonics-Lab/`

## Editing the site

- Page content is in `index.html`, `research.html`, `people.html`, `prospective.html`, `news.html`, and `publications.html`.
- The shared navigation is in `_includes/header.html`.
- The shared footer is in `_includes/footer.html`.
- Shared page metadata and layout are in `_layouts/default.html`.
- Appearance and mobile rules are in `assets/css/style.css`.
- Photographs and figures are stored locally in `assets/images/`.

## Publishing

Keep the repository public and enable GitHub Pages using **GitHub Actions** under **Settings → Pages**.

Every push to `main` builds the Jekyll site, validates local links and image files, and deploys it.

## UMBC migration

See `docs/UMBC_REDIRECT.md` before retiring the old UMBC site.
