const CHAPTERS = [
  { id: "adoration", title: "1 · Adoration" },
  { id: "confession", title: "2 · Confession" },
  { id: "petition", title: "3 · Petition" },
  { id: "thanksgiving", title: "4 · Thanksgiving" },
  { id: "intercession", title: "5 · Intercession" },
  { id: "conclusion", title: "6 · Conclusion" },
];

const state = { heads: null, extras: null, query: "" };

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

async function loadJSON(path) {
  const res = await fetch(path);
  if (!res.ok) throw new Error(`Failed to load ${path}`);
  return res.json();
}

function matches(head, query) {
  if (!query) return true;
  const hay = `${head.id} ${head.title} ${head.pray} ${head.ref}`.toLowerCase();
  return hay.includes(query);
}

function render() {
  const q = state.query.trim().toLowerCase();
  const sections = CHAPTERS.map((chapter) => {
    const heads = (state.heads.sections[chapter.id] || []).filter((head) => matches(head, q));
    if (!heads.length) return "";
    const cards = heads.map((head) => `
      <article class="prompt">
        <h3>${escapeHtml(head.id)} · ${escapeHtml(head.title)}</h3>
        <p class="verse">${escapeHtml(head.pray)}</p>
        <cite>${escapeHtml(head.ref)}</cite>
      </article>
    `).join("");
    return `
      <section class="block">
        <p class="eyebrow">${escapeHtml(chapter.title)}</p>
        <div class="prompts">${cards}</div>
      </section>
    `;
  }).join("");

  const family = (state.extras.family || []).filter((item) => {
    if (!q) return true;
    const hay = `${item.id} ${item.title} ${(item.prayers || []).map((p) => p.text).join(" ")}`.toLowerCase();
    return hay.includes(q);
  }).map((item) => {
    const paras = (item.prayers || []).map((p) => `
      <p class="verse">${escapeHtml(p.text)}</p>
      <cite>${escapeHtml(p.ref)}</cite>
    `).join("");
    return `
      <article class="prompt">
        <h3>${escapeHtml(item.id)} · ${escapeHtml(item.title)}</h3>
        ${paras}
      </article>
    `;
  }).join("");

  const familyBlock = family
    ? `<section class="block">
        <p class="eyebrow">9 · Short forms for a family</p>
        <p class="movement">These stay off the daily sitting. Use them at table, with children, or at the close of the day.</p>
        <div class="prompts">${family}</div>
      </section>`
    : "";

  document.getElementById("catalog").innerHTML = (sections + familyBlock) || `<p class="empty">No heads match.</p>`;
}

async function boot() {
  const [heads, extras] = await Promise.all([
    loadJSON("data/heads.json"),
    loadJSON("data/extras.json"),
  ]);
  state.heads = heads;
  state.extras = extras;
  document.getElementById("lookup").addEventListener("input", (event) => {
    state.query = event.target.value;
    render();
  });
  render();
}

boot().catch((err) => {
  document.getElementById("catalog").innerHTML = `<p class="empty">${escapeHtml(err.message)}</p>`;
});
