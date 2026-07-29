# Redirecting the UMBC website

A redirect from `alokg.umbc.edu` cannot be configured inside this GitHub repository. It must be configured by the administrator of the UMBC WordPress site or web server.

## Preferred method: server-side 301 redirect

Ask UMBC Web Support to permanently redirect:

- `https://alokg.umbc.edu/` → `https://alokghanekar.github.io/`
- `https://alokg.umbc.edu/research/` → `https://alokghanekar.github.io/research.html`
- `https://alokg.umbc.edu/people/` → `https://alokghanekar.github.io/people.html`
- `https://alokg.umbc.edu/prospective-students/` → `https://alokghanekar.github.io/prospective.html`
- `https://alokg.umbc.edu/news/` → `https://alokghanekar.github.io/news.html`
- `https://alokg.umbc.edu/publications/` → `https://alokghanekar.github.io/publications.html`

Use HTTP status **301 (Moved Permanently)**. Retain the redirect for at least one year; keeping it indefinitely is preferable.

Suggested support request:

> Please configure permanent HTTP 301 redirects from the Energy Photonics Lab WordPress site at `https://alokg.umbc.edu/` to the replacement site at `https://alokghanekar.github.io/`. Please preserve the page-level mappings listed above rather than redirecting every old page only to the new homepage.

## Temporary fallback when a 301 redirect is unavailable

Replace the old homepage content with a prominent notice linking to the new site. A meta-refresh can also be used, but it is not equivalent to a server-side 301 redirect:

```html
<link rel="canonical" href="https://alokghanekar.github.io/">
<meta http-equiv="refresh" content="0; url=https://alokghanekar.github.io/">
<p>The Energy Photonics Lab website has moved to
<a href="https://alokghanekar.github.io/">alokghanekar.github.io</a>.</p>
```

Do not delete the UMBC site until the GitHub site has been published, checked on desktop and mobile, and the redirects have been tested.
