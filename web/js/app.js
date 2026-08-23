const THEME_COLORS = {
  chapel: "#1a1612",
  clear: "#f4f1ea",
  spacegray: "#2b303b",
};

const state = {
  date: todayLocal(),
  plan: null,
  method: null,
  heads: null,
  occasional: null,
  extras: null,
  bible: null,
  theme: localStorage.getItem("dp-theme") || "chapel",
  size: localStorage.getItem("dp-size") || "md",
  lesson: localStorage.getItem("dp-lesson") === "nt" ? "nt" : "ot",
};

function todayLocal() {
  const now = new Date();
  return new Date(now.getFullYear(), now.getMonth(), now.getDate());
}

function iso(d) {
  const y = d.getFullYear();
  const m = String(d.getMonth() + 1).padStart(2, "0");
  const day = String(d.getDate()).padStart(2, "0");
  return `${y}-${m}-${day}`;
}

function md(d) {
  return iso(d).slice(5);
}

function parseISODate(value) {
  const [y, m, day] = value.split("-").map(Number);
  return new Date(y, m - 1, day);
}

function addDays(d, delta) {
  const next = new Date(d);
  next.setDate(next.getDate() + delta);
  return next;
}

function dayOfYear(d) {
  const start = new Date(d.getFullYear(), 0, 0);
  return Math.round((d - start) / 86400000);
}

function daysInYear(d) {
  const y = d.getFullYear();
  return (y % 4 === 0 && (y % 100 !== 0 || y % 400 === 0)) ? 366 : 365;
}

function weekdayName(d) {
  return d.toLocaleDateString(undefined, { weekday: "long" });
}

function civilName(d) {
  return d.toLocaleDateString(undefined, {
    weekday: "long",
    month: "long",
    day: "numeric",
    year: "numeric",
  });
}

function lectioKey(d) {
  return `dp-lectio-${iso(d)}`;
}

async function loadJSON(path) {
  const res = await fetch(path);
  if (!res.ok) throw new Error(`Failed to load ${path}`);
  return res.json();
}

async function boot() {
  const [plan, method, heads, occasional, extras, bible] = await Promise.all([
    loadJSON("data/plan.json"),
    loadJSON("data/method.json"),
    loadJSON("data/heads.json"),
    loadJSON("data/occasional.json"),
    loadJSON("data/extras.json"),
    loadJSON("data/bsb.json"),
  ]);
  state.plan = plan;
  state.method = method;
  state.heads = heads;
  state.occasional = occasional;
  state.extras = extras;
  state.bible = bible;
  readHash();
  bind();
  applyAppearance();
  render();
}

function readHash() {
  const raw = location.hash.replace(/^#/, "");
  if (/^\d{4}-\d{2}-\d{2}$/.test(raw)) state.date = parseISODate(raw);
}

function writeHash() {
  const next = `#${iso(state.date)}`;
  if (location.hash !== next) history.replaceState(null, "", next);
}

function bind() {
  document.getElementById("prev-day").addEventListener("click", () => shiftDay(-1));
  document.getElementById("next-day").addEventListener("click", () => shiftDay(1));
  document.getElementById("today").addEventListener("click", () => {
    state.date = todayLocal();
    render();
  });
  document.getElementById("date-input").addEventListener("change", (event) => {
    if (event.target.value) {
      state.date = parseISODate(event.target.value);
      render();
    }
  });
  window.addEventListener("hashchange", () => {
    readHash();
    render();
  });
  document.querySelectorAll("[data-theme]").forEach((button) => {
    button.addEventListener("click", () => {
      state.theme = button.dataset.theme;
      localStorage.setItem("dp-theme", state.theme);
      applyAppearance();
    });
  });
  document.querySelectorAll("[data-size]").forEach((button) => {
    button.addEventListener("click", () => {
      state.size = button.dataset.size;
      localStorage.setItem("dp-size", state.size);
      applyAppearance();
    });
  });
  document.getElementById("office").addEventListener("click", (event) => {
    const lessonTab = event.target.closest("[data-lesson]");
    if (lessonTab) {
      state.lesson = lessonTab.dataset.lesson;
      localStorage.setItem("dp-lesson", state.lesson);
      updateLessonPanel();
      return;
    }
    const toggle = event.target.closest("[data-rollup-toggle]");
    if (!toggle) return;
    const item = toggle.closest(".rollup__item");
    const root = toggle.closest(".rollup");
    const opening = item.getAttribute("aria-expanded") !== "true";
    root.querySelectorAll(":scope > .rollup__item").forEach((el) => {
      el.setAttribute("aria-expanded", "false");
    });
    if (opening) item.setAttribute("aria-expanded", "true");
  });
  document.getElementById("office").addEventListener("input", (event) => {
    const field = event.target.closest("[data-lectio]");
    if (!field) return;
    localStorage.setItem(lectioKey(state.date), field.value);
  });
}

function updateLessonPanel() {
  const root = document.getElementById("scripture");
  if (!root) return;
  const day = lookup();
  if (!day) return;
  root.querySelectorAll("[data-lesson]").forEach((button) => {
    button.classList.toggle("active", button.dataset.lesson === state.lesson);
  });
  const panel = root.querySelector("[data-lesson-panel]");
  if (panel) panel.outerHTML = renderLessonPanel(day);
}

function applyAppearance() {
  const root = document.documentElement;
  root.dataset.theme = state.theme;
  root.dataset.size = state.size;
  document.querySelectorAll("[data-theme]").forEach((button) => {
    button.classList.toggle("is-active", button.dataset.theme === state.theme);
  });
  document.querySelectorAll("[data-size]").forEach((button) => {
    button.classList.toggle("is-active", button.dataset.size === state.size);
  });
  const themeColor = document.querySelector('meta[name="theme-color"]');
  if (themeColor) themeColor.setAttribute("content", THEME_COLORS[state.theme] || THEME_COLORS.chapel);
}

function shiftDay(delta) {
  state.date = addDays(state.date, delta);
  render();
}

function lookup() {
  const key = md(state.date);
  return state.plan.days[key] || null;
}

function openingFor(d) {
  const list = state.method.openings;
  return list[dayOfYear(d) % list.length];
}

function bsb(ref, fallback) {
  if (!ref || !state.bible) return fallback || "";
  try {
    return versesFromRef(state.bible, ref);
  } catch (err) {
    console.warn(err);
    return fallback || "";
  }
}

function verseHtml(item) {
  const ref = item.ref || "";
  const text = bsb(ref, item.pray || item.text || "");
  const cue = item.cue ? `<strong>${escapeHtml(item.cue)}.</strong> ` : "";
  return `${cue}${escapeHtml(text)}${ref ? ` <cite>${escapeHtml(ref)} · BSB</cite>` : ""}`;
}

function todaysHead(sectionId, d) {
  const list = state.heads?.sections?.[sectionId];
  if (!list?.length) return null;
  const index = (dayOfYear(d) - 1) % list.length;
  return { head: list[index], index, total: list.length };
}

function occasionTags(d) {
  const tags = [];
  const weekday = d.getDay();
  if (weekday === 0) tags.push("sunday");
  if (weekday === 6) tags.push("saturday");
  const hour = new Date().getHours();
  if (hour < 12) tags.push("morning");
  if (hour >= 18) tags.push("evening");
  return tags;
}

function splitOccasions(d) {
  const tags = occasionTags(d);
  const items = state.occasional?.items || [];
  const suggested = [];
  const more = [];
  items.forEach((item) => {
    const when = item.when || [];
    if (when.some((tag) => tags.includes(tag))) suggested.push(item);
    else more.push(item);
  });
  return { suggested, more };
}

function render() {
  writeHash();
  const d = state.date;
  document.getElementById("civil-date").textContent = civilName(d);
  document.getElementById("progress").textContent =
    `Day ${dayOfYear(d)} of ${daysInYear(d)} · one office, any hour`;
  document.getElementById("date-input").value = iso(d);
  document.getElementById("office").innerHTML = renderOffice(lookup(), d);
  const field = document.querySelector("[data-lectio]");
  if (field) field.value = localStorage.getItem(lectioKey(d)) || "";
  applyAppearance();
}

function renderOffice(day, d) {
  const opening = openingFor(d);
  const sections = state.method.sections.map((section) => {
    if (section.id === "scripture") return renderScripture(section, day, d);
    return renderPrayerSection(section, d);
  }).join("");

  return `
    <header class="office-head">
      <p class="eyebrow">Daily Prayer</p>
      <h2>${escapeHtml(weekdayName(d))}</h2>
      <p class="lede">A quiet hour after Matthew Henry’s <cite>Method for Prayer</cite>. One sitting. Praise, confess, hear the Word, ask, intercede, and give thanks.</p>
    </header>
    <section class="opening">
      <p class="silence">Begin in silence.</p>
      <p class="sentence">${escapeHtml(bsb(opening.ref, opening.text))} <cite>${escapeHtml(opening.ref)} · BSB</cite></p>
    </section>
    ${renderAlsoToday(d)}
    ${sections}
  `;
}

function renderPrayerSection(section, d) {
  const appointed = todaysHead(section.id, d);
  const headCard = appointed ? renderHeadCard(appointed) : renderStaticPrompts(section);
  const extra = section.id === "thanksgiving" ? renderWeeklyRedemption(d)
    : section.id === "intercession" ? renderStandingIntercession()
    : "";
  const rollup = section.id === "conclusion"
    ? renderParaphrase()
    : renderRollup(section);
  const prayer = section.lords_prayer
    ? `<p class="lords-prayer">${escapeHtml(section.lords_prayer.join(" "))}</p>`
    : "";
  return `
    <section class="block" id="${escapeHtml(section.id)}">
      <p class="eyebrow">${escapeHtml(section.number)}. ${escapeHtml(section.title)}</p>
      <p class="chapter">${escapeHtml(section.chapter)}</p>
      <p class="movement">${escapeHtml(section.movement)}</p>
      ${headCard}
      ${extra}
      ${rollup}
      ${prayer}
    </section>
  `;
}

function renderWeeklyRedemption(d) {
  const list = state.extras?.redemption || [];
  const item = list.find((entry) => entry.weekday === d.getDay()) || list[0];
  if (!item) return "";
  return `
    <article class="prompt prompt--week">
      <p class="head-today">This week’s mercy · ${escapeHtml(weekdayName(d))}</p>
      <h3>${escapeHtml(item.title)}</h3>
      <p class="verse">${escapeHtml(bsb(item.ref, item.pray))}</p>
      <cite>${escapeHtml(item.ref)} · BSB</cite>
    </article>
  `;
}

function renderStandingIntercession() {
  const items = state.extras?.intercession || [];
  if (!items.length) return "";
  const paras = items.map((item) => `
      <p class="rollup__verse">${verseHtml(item)}</p>
    `).join("");
  return `
    <div class="rollup" data-rollup="intercession-standing">
      <div class="rollup__item" aria-expanded="false">
        <button type="button" class="rollup__toggle" data-rollup-toggle>
          <span>Pray also for nations, the persecuted, ministers, rulers, and the lost</span>
          <span class="rollup__chevron" aria-hidden="true"></span>
        </button>
        <div class="rollup__body">${paras}</div>
      </div>
    </div>
  `;
}

function renderParaphrase() {
  const items = state.extras?.paraphrase || [];
  if (!items.length) return "";
  const paras = items.map((item) => `
      <p class="rollup__verse">${verseHtml(item)}</p>
    `).join("");
  return `
    <div class="rollup" data-rollup="paraphrase">
      <div class="rollup__item" aria-expanded="false">
        <button type="button" class="rollup__toggle" data-rollup-toggle>
          <span>Pray the Lord’s Prayer open</span>
          <span class="rollup__chevron" aria-hidden="true"></span>
        </button>
        <div class="rollup__body">${paras}</div>
      </div>
    </div>
  `;
}

function renderHeadCard(appointed) {
  const { head, index, total } = appointed;
  return `
    <article class="prompt prompt--today">
      <p class="head-today">Today’s head · ${escapeHtml(head.id)} · ${index + 1} of ${total}</p>
      <h3>${escapeHtml(head.title)}</h3>
      <p class="verse">${escapeHtml(bsb(head.ref, head.pray))}</p>
      <cite>${escapeHtml(head.ref)} · BSB</cite>
    </article>
  `;
}

function renderStaticPrompts(section) {
  const prompts = (section.prompts || []).map((item) => `
    <article class="prompt">
      <h3>${escapeHtml(item.cue)}</h3>
      <p class="verse">${escapeHtml(bsb(item.ref, item.pray))}</p>
      <cite>${escapeHtml(item.ref)} · BSB</cite>
    </article>
  `).join("");
  return prompts ? `<div class="prompts">${prompts}</div>` : "";
}

function renderRollup(section) {
  const prayers = section.rollup;
  if (!prayers?.length) return "";
  const paras = prayers.map((item) => `
      <p class="rollup__verse">${verseHtml(item)}</p>
    `).join("");
  return `
    <div class="rollup" data-rollup="${escapeHtml(section.id)}">
      <div class="rollup__item" aria-expanded="false">
        <button type="button" class="rollup__toggle" data-rollup-toggle>
          <span>Prayers for ${escapeHtml(section.title)}</span>
          <span class="rollup__chevron" aria-hidden="true"></span>
        </button>
        <div class="rollup__body">${paras}</div>
      </div>
    </div>
  `;
}

function renderScripture(section, day, d) {
  if (!day) {
    return `
      <section class="block" id="scripture">
        <p class="eyebrow">${escapeHtml(section.number)}. ${escapeHtml(section.title)}</p>
        <p class="empty">No reading is listed for this date.</p>
      </section>
    `;
  }
  const weekend = day.weekend
    ? `<p class="lessons__note">This date carries a Tabletalk weekend block — the same Old and New Testament stretch as its neighboring catch-up day. Read it once across the two days, or in one sitting.</p>`
    : "";
  const otActive = state.lesson === "ot" ? " active" : "";
  const ntActive = state.lesson === "nt" ? " active" : "";
  return `
    <section class="block lessons" id="scripture">
      <p class="eyebrow">${escapeHtml(section.number)}. ${escapeHtml(section.title)}</p>
      <p class="chapter">${escapeHtml(section.chapter)}</p>
      <p class="movement">${escapeHtml(section.movement)}</p>
      ${renderRollup(section)}
      ${weekend}
      <div data-function="option-selector">
        <p class="option-selector-wrapper">
          <button type="button" class="option-selector${otActive}" data-lesson="ot">OT</button>
          <button type="button" class="option-selector${ntActive}" data-lesson="nt">NT</button>
        </p>
        ${renderLessonPanel(day)}
      </div>
      ${renderLectio(day)}
    </section>
  `;
}

function renderLessonPanel(day) {
  const isOt = state.lesson !== "nt";
  const title = isOt ? "Old Testament" : "New Testament";
  const ref = isOt ? day.ot : day.nt;
  const url = gatewayUrl(ref);
  const search = gatewaySearch(ref);
  return `
        <div class="lesson-panel" data-lesson-panel>
          <h3>${escapeHtml(title)} <span>${escapeHtml(ref)}</span></h3>
          <p class="lesson-panel__kicker">NKJV · BibleGateway</p>
          <p class="lesson-panel__ref">${escapeHtml(search)}</p>
          <a class="lesson-link" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer">
            Open ${escapeHtml(ref)} in NKJV
          </a>
        </div>
  `;
}

function renderLectio(day) {
  return `
    <div class="lectio">
      <p class="eyebrow">Turn a phrase</p>
      <p class="movement">Henry’s method is to pray this Scripture, not only the stock heads. From <strong>${escapeHtml(day.ot)}</strong> and <strong>${escapeHtml(day.nt)}</strong>, notice a line. Carry it into the petitions that follow.</p>
      <ul class="lectio__cues">
        <li>Praise a word about God</li>
        <li>Confess where it searches you</li>
        <li>Ask for what it commands</li>
        <li>Give thanks for a promise</li>
      </ul>
      <label class="lectio__label" for="lectio-note">A phrase to carry into prayer</label>
      <textarea id="lectio-note" class="lectio__note" data-lectio rows="3" placeholder="Write a line from today’s reading…"></textarea>
    </div>
  `;
}

function renderOccasion(item, suggested) {
  const paras = (item.prayers || []).map((p) => `
      <p class="rollup__verse">${verseHtml(p)}</p>
    `).join("");
  const badge = suggested ? `<span class="also__badge">For today</span>` : "";
  return `
    <div class="rollup" data-rollup="${escapeHtml(item.id)}">
      <div class="rollup__item" aria-expanded="false">
        <button type="button" class="rollup__toggle" data-rollup-toggle>
          <span>${escapeHtml(item.id)} · ${escapeHtml(item.title)} ${badge}</span>
          <span class="rollup__chevron" aria-hidden="true"></span>
        </button>
        <div class="rollup__body">${paras}</div>
      </div>
    </div>
  `;
}

function renderAlsoToday(d) {
  const { suggested, more } = splitOccasions(d);
  const suggestedHtml = suggested.map((item) => renderOccasion(item, true)).join("");
  const moreHtml = more.map((item) => renderOccasion(item, false)).join("");
  return `
    <section class="also" id="also-today">
      <p class="eyebrow">Also today</p>
      <p class="movement">Henry’s occasional addresses. Open only what the day needs — Lord’s Day, a meal, a journey, sickness, or a burden.</p>
      ${suggestedHtml}
      <div class="rollup" data-rollup="occasions-more">
        <div class="rollup__item" aria-expanded="false">
          <button type="button" class="rollup__toggle" data-rollup-toggle>
            <span>More occasions</span>
            <span class="rollup__chevron" aria-hidden="true"></span>
          </button>
          <div class="rollup__body also__more">${moreHtml}</div>
        </div>
      </div>
    </section>
  `;
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("sw.js").catch(() => {});
}

boot().catch((err) => {
  document.getElementById("office").innerHTML = `<p class="empty">${escapeHtml(err.message)}</p>`;
});
