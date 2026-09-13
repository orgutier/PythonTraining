(function () {
  "use strict";

  const listEl = document.getElementById("topicList");
  const detailEl = document.getElementById("topicDetail");
  const searchEl = document.getElementById("searchBox");
  const sidebarEl = document.getElementById("sidebar");
  const navToggle = document.getElementById("navToggle");

  const drawerEl = document.getElementById("glossaryDrawer");
  const drawerBackdropEl = document.getElementById("drawerBackdrop");
  const drawerCategoryEl = document.getElementById("drawerCategory");
  const drawerTermEl = document.getElementById("drawerTerm");
  const drawerBodyEl = document.getElementById("drawerBody");
  const drawerCloseBtn = document.getElementById("drawerClose");

  let currentIndex = 0;
  let lastFocusedBadge = null;

  const META_GROUPS = [
    { key: "keywords", heading: "Keywords & syntax", badgeClass: "" },
    { key: "methods", heading: "Methods & attributes", badgeClass: "method" },
    { key: "dunders", heading: "Special methods (dunders)", badgeClass: "dunder" },
    { key: "modules", heading: "Modules", badgeClass: "module" },
    { key: "concepts", heading: "Concepts", badgeClass: "concept" },
    { key: "theory", heading: "Theory & internals", badgeClass: "theory" }
  ];

  function renderList() {
    listEl.innerHTML = "";
    TOPICS.forEach((topic, i) => {
      const li = document.createElement("li");
      li.className = "topic-item" + (i === currentIndex ? " active" : "");
      li.dataset.index = i;

      const btn = document.createElement("button");
      btn.type = "button";
      btn.setAttribute("aria-current", i === currentIndex ? "true" : "false");
      btn.innerHTML =
        '<span class="num">' + String(topic.n).padStart(2, "0") + '</span>' +
        '<span class="label"><span class="title">' + escapeHtml(topic.title) +
        '</span><span class="sub">' + escapeHtml(topic.sub) + '</span></span>';
      btn.addEventListener("click", () => selectTopic(i));

      li.appendChild(btn);
      listEl.appendChild(li);
    });
  }

  function tierBlock(cls, label, tier) {
    if (!tier || (!tier.text && !tier.ref)) {
      return '<div class="tier ' + cls + '"><h2>' + label + '</h2><p class="empty-tier">Not applicable this topic.</p></div>';
    }
    let html = '<div class="tier ' + cls + '"><h2>' + label + '</h2>';
    if (tier.text) html += "<p>" + escapeHtml(tier.text) + "</p>";
    if (tier.ref) html += '<p class="ref">' + escapeHtml(tier.ref) + "</p>";
    html += "</div>";
    return html;
  }

  function makeBadge(term, badgeClass) {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "badge" + (badgeClass ? " " + badgeClass : "");
    btn.textContent = term;
    btn.addEventListener("click", () => openGlossary(term, btn));
    return btn;
  }

  function buildMetaRow(topic) {
    const groupsWithContent = META_GROUPS.filter((g) => topic[g.key] && topic[g.key].length);
    if (groupsWithContent.length === 0) return null;

    const row = document.createElement("div");
    row.className = "meta-row";

    groupsWithContent.forEach((g) => {
      const block = document.createElement("div");
      block.className = "meta-block";

      const h3 = document.createElement("h3");
      h3.textContent = g.heading;
      block.appendChild(h3);

      const badges = document.createElement("div");
      badges.className = "badges";
      topic[g.key].forEach((term) => badges.appendChild(makeBadge(term, g.badgeClass)));
      block.appendChild(badges);

      row.appendChild(block);
    });

    return row;
  }

  function renderDetail(topic) {
    let html = "";
    html += '<div class="topic-head">';
    html += '<div class="num">Topic ' + String(topic.n).padStart(2, "0") + " of " + TOPICS.length + "</div>";
    html += "<h1>" + escapeHtml(topic.title) + "</h1>";
    html += '<div class="sub">' + escapeHtml(topic.sub) + "</div>";
    html += "</div>";

    html += tierBlock("basic", "Basic knowledge", topic.basic);
    html += tierBlock("mid", "Mid-level knowledge", topic.mid);
    html += tierBlock("advanced", "Advanced knowledge", topic.advanced);

    if (topic.internals) {
      html += '<div class="internals"><h2>Python internals — how it actually works</h2><p>' +
        escapeHtml(topic.internals) + "</p></div>";
    }

    if (topic.note) {
      html += '<div class="note">' + escapeHtml(topic.note) + "</div>";
    }

    detailEl.innerHTML = html;

    const metaRow = buildMetaRow(topic);
    if (metaRow) {
      detailEl.appendChild(metaRow);
    }

    document.getElementById("main").scrollTop = 0;
  }

  function selectTopic(index) {
    currentIndex = index;
    renderList();
    renderDetail(TOPICS[index]);
    closeGlossary();
    if (window.innerWidth <= 860) {
      sidebarEl.classList.remove("open");
      navToggle.setAttribute("aria-expanded", "false");
    }
  }

  function escapeHtml(str) {
    const div = document.createElement("div");
    div.textContent = str;
    return div.innerHTML;
  }

  function filterList(query) {
    const q = query.trim().toLowerCase();
    const items = listEl.querySelectorAll(".topic-item");
    items.forEach((li) => {
      const i = Number(li.dataset.index);
      const topic = TOPICS[i];
      const haystack = [
        topic.title, topic.sub,
        ...(topic.keywords || []), ...(topic.methods || []),
        ...(topic.dunders || []), ...(topic.modules || []),
        ...(topic.concepts || []), ...(topic.theory || [])
      ].join(" ").toLowerCase();
      li.classList.toggle("hidden", q.length > 0 && !haystack.includes(q));
    });
  }

  /* ------------------------------------------------------------ */
  /* Glossary drawer                                                */
  /* ------------------------------------------------------------ */

  function renderGlossaryBody(term, entry) {
    let html = "";
    if (entry.summary) html += "<p class='drawer-summary'>" + escapeHtml(entry.summary) + "</p>";
    if (entry.usage) {
      html += "<h3>How &amp; when to use it</h3><p>" + escapeHtml(entry.usage) + "</p>";
    }
    if (entry.example) {
      html += "<h3>Example</h3><pre class='drawer-code'><code>" + escapeHtml(entry.example) + "</code></pre>";
    }
    if (entry.related && entry.related.length) {
      html += "<h3>Related</h3><div class='badges drawer-related' id='drawerRelated'></div>";
    }
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
      drawerBodyEl.innerHTML = "<p class='drawer-summary'>No dedicated entry yet for <strong>" +
        escapeHtml(term) + "</strong>. Check the official Python docs for details.</p>";
    }

    drawerEl.classList.add("open");
    drawerEl.setAttribute("aria-hidden", "false");
    drawerBackdropEl.hidden = false;
    requestAnimationFrame(() => drawerBackdropEl.classList.add("visible"));
    drawerCloseBtn.focus();
  }

  function closeGlossary() {
    if (!drawerEl.classList.contains("open")) return;
    drawerEl.classList.remove("open");
    drawerEl.setAttribute("aria-hidden", "true");
    drawerBackdropEl.classList.remove("visible");
    drawerBackdropEl.hidden = true;
    if (lastFocusedBadge && document.body.contains(lastFocusedBadge)) {
      lastFocusedBadge.focus();
    }
  }

  drawerCloseBtn.addEventListener("click", closeGlossary);
  drawerBackdropEl.addEventListener("click", closeGlossary);

  searchEl.addEventListener("input", (e) => filterList(e.target.value));

  navToggle.addEventListener("click", () => {
    const open = sidebarEl.classList.toggle("open");
    navToggle.setAttribute("aria-expanded", open ? "true" : "false");
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && drawerEl.classList.contains("open")) {
      closeGlossary();
      return;
    }
    if (e.target === searchEl) return;
    if (e.key === "ArrowDown") {
      e.preventDefault();
      selectTopic(Math.min(currentIndex + 1, TOPICS.length - 1));
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      selectTopic(Math.max(currentIndex - 1, 0));
    }
  });

  renderList();
  renderDetail(TOPICS[0]);
})();
