#!/usr/bin/env python3
"""Validate generated site files without making network requests."""
from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

REMOTE_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}
ATTRS = {"href", "src", "poster"}

class ReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name in ATTRS and value:
                self.references.append((name, value.strip()))


def candidate_paths(site: Path, page: Path, raw: str, baseurl: str) -> list[Path]:
    parsed = urlsplit(raw)
    if parsed.scheme.lower() in REMOTE_SCHEMES or raw.startswith("#") or raw.startswith("//"):
        return []
    path_text = unquote(parsed.path)
    if not path_text:
        return []
    if baseurl and (path_text == baseurl or path_text.startswith(f"{baseurl}/")):
        path_text = path_text[len(baseurl):] or "/"
    if path_text.startswith("/"):
        target = site / path_text.lstrip("/")
    else:
        target = page.parent / path_text
    target = target.resolve()
    candidates = [target]
    if path_text.endswith("/"):
        candidates.append(target / "index.html")
    elif not target.suffix:
        candidates.extend([target.with_suffix(".html"), target / "index.html"])
    return candidates


def verify_image(path: Path) -> str | None:
    data = path.read_bytes()
    if not data:
        return "image is empty"
    suffix = path.suffix.lower()
    if suffix in {".jpg", ".jpeg"} and not (data.startswith(b"\xff\xd8") and data.endswith(b"\xff\xd9")):
        return "invalid JPEG signature"
    if suffix == ".png" and not data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "invalid PNG signature"
    if suffix == ".svg" and b"<svg" not in data[:1000]:
        return "invalid SVG content"
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", nargs="?", default="_site", help="generated site directory")
    parser.add_argument(
        "--baseurl",
        default="",
        help="published project path, for example /Energy-Photonics-Lab",
    )
    args = parser.parse_args()
    site = Path(args.site).resolve()
    baseurl = "/" + args.baseurl.strip("/") if args.baseurl.strip("/") else ""
    if not site.is_dir():
        print(f"ERROR: site directory not found: {site}")
        return 2

    errors: list[str] = []
    html_files = sorted(site.rglob("*.html"))
    if not html_files:
        errors.append("No HTML pages were generated.")

    for page in html_files:
        text = page.read_text(encoding="utf-8")
        if "alokg.umbc.edu/wp-content/uploads" in text:
            errors.append(f"{page.relative_to(site)} still references UMBC-hosted media")
        parser = ReferenceParser()
        parser.feed(text)
        for attr, raw in parser.references:
            candidates = candidate_paths(site, page, raw, baseurl)
            if candidates and not any(p.exists() for p in candidates):
                shown = ", ".join(str(p.relative_to(site)) if p.is_relative_to(site) else str(p) for p in candidates)
                errors.append(f"{page.relative_to(site)}: missing {attr}={raw!r}; checked {shown}")

    image_extensions = {".jpg", ".jpeg", ".png", ".svg", ".webp", ".gif"}
    images = [p for p in site.rglob("*") if p.suffix.lower() in image_extensions]
    for image in images:
        problem = verify_image(image)
        if problem:
            errors.append(f"{image.relative_to(site)}: {problem}")

    if errors:
        print("Site validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(html_files)} HTML pages and {len(images)} images.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
