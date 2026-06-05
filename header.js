// ============================================================
// To change the lab name, edit ONLY the line below:
const LAB_NAME = "Energy Photonics Labv";

// To change the sub-title line, edit this:
const LAB_SUB = "Department of Mechanical Engineering &nbsp;&middot;&nbsp; University of Maryland, Baltimore County";
// ============================================================

const NAV = [
  ["index.html",       "Home"],
  ["research.html",    "Research"],
  ["people.html",      "People"],
  ["prospective.html", "Prospective Students"],
  ["news.html",        "News"],
  ["publications.html","Publications"],
];

const current = window.location.pathname.split("/").pop() || "index.html";

const links = NAV.map(([href, label]) =>
  `<a href="${href}"${href === current ? ' class="active"' : ""}>${label}</a>`
).join("\n    ");

document.getElementById("site-header").innerHTML = `
<header>
  <div class="lab-name">${LAB_NAME}</div>
  <div class="lab-sub">${LAB_SUB}</div>
  <nav>
    ${links}
  </nav>
</header>`;

document.title = document.title.replace(/^.*?–/, LAB_NAME + " –");
