(function () {
  "use strict";

  const listEl = document.getElementById("topicList");
  const detailEl = document.getElementById("topicDetail");
  const searchEl = document.getElementById("searchBox");
  const sidebarEl = document.getElementById("sidebar");
  const navToggle = document.getElementById("navToggle");

  const drawerEl = document.getElementById("glossaryDrawer");
  const drawerCategoryEl = document.getElementById("drawerCategory");
  const drawerTermEl = document.getElementById("drawerTerm");
  const drawerBodyEl = document.getElementById("drawerBody");
  const drawerCloseBtn = document.getElementById("drawerClose");

  let currentIndex = 0;
  let lastFocusedBadge = null;

  const CAT_CLASS = { keywords: "", dunders: "dunder", modules: "module", methods: "method", concepts: "concept", theory: "theory" };
  const CAT_HEADING = { keywords: "Keywords & syntax", dunders: "Special methods (dunders)", modules: "Modules", methods: "Methods & attributes", concepts: "Concepts", theory: "Theory & internals" };
  const CATS = ["keywords", "dunders", "modules", "methods", "concepts", "theory"];

  // ------------------------------------------------------------------
  // Build the flat sidebar list: 14 stages, then 3 exams.
  // ------------------------------------------------------------------
  const ENTRIES = [];
  REVIEW_DATA.stages.forEach((s) => {
    ENTRIES.push({ kind: "stage", n: s.n, title: "Stage " + String(s.n).padStart(2, "0"), sub: s.title, data: s });
  });
  ["exam01", "exam02", "exam03"].forEach((eid, i) => {
    const e = REVIEW_DATA.exams[eid];
    if (!e) return;
    ENTRIES.push({ kind: "exam", n: 100 + i, title: "Exam " + (i + 1), sub: "Covers Stages " + e.lo + "-" + e.hi, data: e });
  });

  function escapeHtml(str) {
    const div = document.createElement("div");
    div.textContent = str == null ? "" : String(str);
    return div.innerHTML;
  }

  function anyBadges(bucket) {
    return bucket && CATS.some((c) => bucket[c] && bucket[c].length);
  }

  function makeBadge(term, badgeClass) {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "badge" + (badgeClass ? " " + badgeClass : "");
    btn.textContent = term;
    btn.addEventListener("click", () => openGlossary(term, btn));
    return btn;
  }

  function badgeGroup(bucket) {
    const wrap = document.createElement("div");
    wrap.className = "badges";
    CATS.forEach((cat) => {
      (bucket[cat] || []).forEach((term) => wrap.appendChild(makeBadge(term, CAT_CLASS[cat])));
    });
    return wrap;
  }

  // ------------------------------------------------------------------
  // Sidebar
  // ------------------------------------------------------------------
  function renderList() {
    listEl.innerHTML = "";
    ENTRIES.forEach((entry, i) => {
      const li = document.createElement("li");
      li.className = "topic-item" + (i === currentIndex ? " active" : "");
      li.dataset.index = i;

      const btn = document.createElement("button");
      btn.type = "button";
      btn.setAttribute("aria-current", i === currentIndex ? "true" : "false");
      btn.innerHTML =
        '<span class="num">' + (entry.kind === "exam" ? "Ex" : String(entry.n).padStart(2, "0")) + '</span>' +
        '<span class="label"><span class="title">' + escapeHtml(entry.title) +
        '</span><span class="sub">' + escapeHtml(entry.sub) + '</span></span>';
      btn.addEventListener("click", () => selectTopic(i));

      li.appendChild(btn);
      listEl.appendChild(li);
    });
  }

  function selectTopic(index) {
    currentIndex = index;
    renderList();
    renderDetail(ENTRIES[index]);
    if (window.innerWidth <= 860) {
      sidebarEl.classList.remove("open");
      navToggle.setAttribute("aria-expanded", "false");
    }
  }

  function filterList(query) {
    const q = query.trim().toLowerCase();
    const items = listEl.querySelectorAll(".topic-item");
    items.forEach((li) => {
      const i = Number(li.dataset.index);
      const entry = ENTRIES[i];
      const haystack = (entry.title + " " + entry.sub).toLowerCase();
      li.classList.toggle("hidden", q.length > 0 && !haystack.includes(q));
    });
  }

  // ------------------------------------------------------------------
  // Tier block: New / Refresh / tier-only-new / exercises
  // ------------------------------------------------------------------
  function tierNode(tier) {
    const wrap = document.createElement("div");
    wrap.className = "review-tier";

    const h2 = document.createElement("h2");
    h2.textContent = tier.label;
    wrap.appendChild(h2);

    const hasNew = anyBadges(tier.newItems);
    const hasRefresh = anyBadges(tier.refreshItems);

    if (hasNew) {
      const sec = document.createElement("div");
      sec.className = "review-section new";
      sec.innerHTML = '<h3 class="review-label new-label">New this tier</h3>';
      sec.appendChild(badgeGroup(tier.newItems));
      if (tier.ref) {
        const p = document.createElement("p");
        p.className = "ref";
        p.textContent = tier.ref;
        sec.appendChild(p);
      }
      wrap.appendChild(sec);
    }

    if (hasRefresh) {
      const sec = document.createElement("div");
      sec.className = "review-section refresh";
      sec.innerHTML = '<h3 class="review-label refresh-label">Refresh (covered earlier)</h3>';
      sec.appendChild(badgeGroup(tier.refreshItems));
      wrap.appendChild(sec);
    }

    if (!hasNew && !hasRefresh) {
      wrap.insertAdjacentHTML("beforeend", '<p class="empty-tier">No tagged keywords/concepts for this tier yet in the source data.</p>');
    }

    if (tier.exercises && tier.exercises.length) {
      const exWrap = document.createElement("div");
      exWrap.className = "review-exercises";
      tier.exercises.forEach((ex) => exWrap.appendChild(exerciseCard(ex)));
      wrap.appendChild(exWrap);
    }

    if (anyBadges(tier.tierOnlyNew)) {
      const sec = document.createElement("div");
      sec.className = "review-section tier-only";
      sec.innerHTML = '<h3 class="review-label">Also new this tier (from the lesson, not tied to one exercise’s code)</h3>';
      sec.appendChild(badgeGroup(tier.tierOnlyNew));
      wrap.appendChild(sec);
    }

    return wrap;
  }

  function exerciseCard(ex) {
    const card = document.createElement("div");
    card.className = "exercise-card";
    card.innerHTML =
      '<div class="exercise-id">' + escapeHtml(ex.id) + '</div>' +
      '<h4>' + escapeHtml(ex.title) + '</h4>' +
      '<p class="exercise-summary">' + escapeHtml(ex.summary) + '</p>';
    if (anyBadges(ex.newItems)) {
      card.insertAdjacentHTML("beforeend", '<div class="exercise-new-label">Introduces</div>');
      card.appendChild(badgeGroup(ex.newItems));
    } else {
      card.insertAdjacentHTML("beforeend", '<p class="exercise-none">Practices this tier’s tools without introducing a new one of its own.</p>');
    }
    return card;
  }

  function capstoneNode(stage) {
    const wrap = document.createElement("div");
    wrap.className = "review-tier";
    wrap.innerHTML = '<h2>Synthesis stage — no new material</h2><p>' + escapeHtml(stage.note) + '</p>';
    if (stage.newConcepts && stage.newConcepts.length) {
      const sec = document.createElement("div");
      sec.className = "review-section new";
      sec.innerHTML = '<h3 class="review-label new-label">New concept</h3>';
      const b = emptyBucket();
      b.concepts = stage.newConcepts;
      sec.appendChild(badgeGroup(b));
      wrap.appendChild(sec);
    }
    wrap.insertAdjacentHTML("beforeend",
      '<div class="review-section refresh"><h3 class="review-label refresh-label">Refresh</h3>' +
      '<p class="capstone-refresh-note">Everything from Stages 1–13 is fair game — see each stage’s own page in this reference for its full list.</p></div>');
    return wrap;
  }

  function emptyBucket() {
    const o = {};
    CATS.forEach((c) => (o[c] = []));
    return o;
  }

  function challengeCard(c) {
    const div = document.createElement("div");
    div.className = "challenge";
    div.innerHTML =
      '<div class="challenge-tag">Interview Challenge &mdash; ' + escapeHtml(c.id) + '</div>' +
      '<h2>' + escapeHtml(c.title) + '</h2>' +
      '<p>' + escapeHtml(c.blurb) + '</p>';
    if (anyBadges(c.refreshItems)) {
      div.insertAdjacentHTML("beforeend", '<h3 class="review-label refresh-label">Practices (from earlier stages)</h3>');
      div.appendChild(badgeGroup(c.refreshItems));
    }
    div.insertAdjacentHTML("beforeend", '<p class="challenge-note">Based on this challenge’s own reference solution — you’re free to solve it a different way.</p>');
    return div;
  }

  // ------------------------------------------------------------------
  // Top-level render
  // ------------------------------------------------------------------
  function renderStageDetail(entry) {
    const stage = entry.data;
    detailEl.innerHTML = "";
    detailEl.insertAdjacentHTML("beforeend",
      '<div class="topic-head">' +
      '<div class="num">' + entry.title + '</div>' +
      '<h1>' + escapeHtml(stage.title) + '</h1>' +
      '<div class="sub">' + escapeHtml(stage.sub) + '</div>' +
      '</div>'
    );

    if (stage.isCapstone) {
      detailEl.appendChild(capstoneNode(stage));
    } else {
      stage.tiers.forEach((tier) => detailEl.appendChild(tierNode(tier)));
    }

    const stageNum = String(stage.n).padStart(2, "0");
    const challengeIds = Object.keys(REVIEW_DATA.challenges).filter((cid) => REVIEW_DATA.challenges[cid].stage === "stage" + stageNum);
    if (challengeIds.length) {
      const h2 = document.createElement("h2");
      h2.className = "challenges-heading";
      h2.textContent = "Interview challenges for this stage";
      detailEl.appendChild(h2);
      challengeIds.forEach((cid) => detailEl.appendChild(challengeCard(REVIEW_DATA.challenges[cid])));
    }

    document.getElementById("main").scrollTop = 0;
  }

  function renderExamDetail(entry) {
    const exam = entry.data;
    detailEl.innerHTML = "";
    detailEl.insertAdjacentHTML("beforeend",
      '<div class="topic-head">' +
      '<div class="num">' + entry.title + '</div>' +
      '<h1>' + escapeHtml(entry.title) + '</h1>' +
      '<div class="sub">' + escapeHtml(entry.sub) + '</div>' +
      '</div>'
    );
    const wrap = document.createElement("div");
    wrap.className = "review-tier";
    wrap.innerHTML = '<h2>Pure review — no new material</h2><p class="capstone-refresh-note">An exam re-assesses everything from the stages it covers; nothing here is introduced for the first time.</p>';
    const sec = document.createElement("div");
    sec.className = "review-section refresh";
    sec.innerHTML = '<h3 class="review-label refresh-label">Covered by this exam’s reference solution</h3>';
    sec.appendChild(badgeGroup(exam.refreshItems));
    wrap.appendChild(sec);
    detailEl.appendChild(wrap);
    document.getElementById("main").scrollTop = 0;
  }

  function renderDetail(entry) {
    if (entry.kind === "exam") renderExamDetail(entry);
    else renderStageDetail(entry);
  }

  // ------------------------------------------------------------------
  // Glossary drawer (identical mechanism to presentation/script.js,
  // sharing the same GLOSSARY data so a term's details never drift
  // between the two presentations).
  // ------------------------------------------------------------------
  function codeBlockHtml(code, filename) {
    const highlighted = (typeof highlightPython === "function") ? highlightPython(code) : escapeHtml(code);
    return '<div class="vscode-block">' +
      '<div class="vscode-titlebar">' +
      '<span class="vscode-dot red"></span><span class="vscode-dot yellow"></span><span class="vscode-dot green"></span>' +
      '<span class="vscode-filename">' + escapeHtml(filename || "example.py") + "</span>" +
      "</div>" +
      '<pre class="vscode-code"><code>' + highlighted + "</code></pre>" +
      "</div>";
  }

  function openDrawer() {
    drawerEl.classList.add("open");
    drawerEl.setAttribute("aria-hidden", "false");
    drawerCloseBtn.focus();
  }

  function renderGlossaryBody(term, entry) {
    let html = "";
    if (entry.summary) html += "<p class='drawer-summary'>" + escapeHtml(entry.summary) + "</p>";
    if (entry.usage) html += "<h3>How &amp; when to use it</h3><p>" + escapeHtml(entry.usage) + "</p>";
    if (entry.example) html += "<h3>Example</h3>" + codeBlockHtml(entry.example, term + ".py");
    if (entry.related && entry.related.length) html += "<h3>Related</h3><div class='badges drawer-related' id='drawerRelated'></div>";
    drawerBodyEl.innerHTML = html;

    if (entry.related && entry.related.length) {
      const relatedWrap = document.getElementById("drawerRelated");
      const classForCategory = { method: "method", dunder: "dunder", module: "module", concept: "concept", theory: "theory" };
      entry.related.forEach((relTerm) => {
        const relEntry = (typeof GLOSSARY !== "undefined") && GLOSSARY[relTerm];
        const relClass = relEntry ? (classForCategory[relEntry.category] || "") : "";
        relatedWrap.appendChild(makeBadge(relTerm, relClass));
      });
    }
  }

  function openGlossary(term, triggerEl) {
    const entry = (typeof GLOSSARY !== "undefined") && GLOSSARY[term];
    lastFocusedBadge = triggerEl || lastFocusedBadge;

    drawerTermEl.textContent = term;
    if (entry) {
      const label = (typeof GLOSSARY_CATEGORY_LABELS !== "undefined" && GLOSSARY_CATEGORY_LABELS[entry.category]) || entry.category;
      drawerCategoryEl.textContent = label;
      drawerCategoryEl.className = "drawer-category cat-" + entry.category;
      renderGlossaryBody(term, entry);
    } else {
      drawerCategoryEl.textContent = "Term";
      drawerCategoryEl.className = "drawer-category";
      drawerBodyEl.innerHTML = "<p class='drawer-summary'>No dedicated entry yet for <strong>" + escapeHtml(term) + "</strong>. Check the official Python docs for details.</p>";
    }
    openDrawer();
  }

  function closeGlossary() {
    if (!drawerEl.classList.contains("open")) return;
    drawerEl.classList.remove("open");
    drawerEl.setAttribute("aria-hidden", "true");
    if (lastFocusedBadge && document.body.contains(lastFocusedBadge)) lastFocusedBadge.focus();
  }

  drawerCloseBtn.addEventListener("click", closeGlossary);
  searchEl.addEventListener("input", (e) => filterList(e.target.value));
  navToggle.addEventListener("click", () => {
    const open = sidebarEl.classList.toggle("open");
    navToggle.setAttribute("aria-expanded", open ? "true" : "false");
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && drawerEl.classList.contains("open")) { closeGlossary(); return; }
    if (e.target === searchEl) return;
    if (e.key === "ArrowDown") { e.preventDefault(); selectTopic(Math.min(currentIndex + 1, ENTRIES.length - 1)); }
    else if (e.key === "ArrowUp") { e.preventDefault(); selectTopic(Math.max(currentIndex - 1, 0)); }
  });

  renderList();
  renderDetail(ENTRIES[0]);
})();
