# Validation report

Validation completed on July 29, 2026.

## Checks completed

- Parsed and rendered all seven HTML pages: Home, Research, People, Prospective Students, News, Publications, and 404.
- Verified that each rendered page has exactly one `h1` and no duplicate HTML IDs.
- Verified that every image has alternative text.
- Verified all local page, stylesheet, favicon, and image references.
- Verified that generated navigation, stylesheet, image, canonical, sitemap, and
  social-preview URLs include the `/Energy-Photonics-Lab` project path.
- Verified the integrity of all JPEG, PNG, and SVG image files.
- Confirmed that published page source contains no references to `alokg.umbc.edu/wp-content/uploads`.
- Reviewed desktop rendering at 1440 pixels wide.
- Reviewed mobile rendering at 390 pixels wide.

## Automated deployment check

The GitHub Actions workflow builds the site with Jekyll and then runs `scripts/check_site.py` against the generated `_site` directory before deployment. A missing local file or invalid image causes the build to fail rather than publishing a broken update.

## Remaining external action

The old UMBC address must be redirected by UMBC Web Support or the UMBC WordPress administrator. See `UMBC_REDIRECT.md`.
