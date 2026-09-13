(function () {
  "use strict";

  const listEl = document.getElementById("topicList");
  const detailEl = document.getElementById("topicDetail");
  const searchEl = document.getElementById("searchBox");
  const sidebarEl = document.getElementById("sidebar");
  const navToggle = document.getElementById("navToggle");

  let currentIndex = 0;

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

  function badgeList(items, extraClass) {
    if (!items || items.length === 0) return "";
    return items
      .map((k) => '<span class="badge ' + (extraClass || "") + '">' + escapeHtml(k) + "</span>")
      .join("");
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

    const hasMeta = (topic.keywords && topic.keywords.length) ||
      (topic.dunders && topic.dunders.length) ||
      (topic.modules && topic.modules.length);

    if (hasMeta) {
      html += '<div class="meta-row">';
      if (topic.keywords && topic.keywords.length) {
        html += '<div class="meta-block"><h3>Keywords &amp; syntax</h3><div class="badges">' +
          badgeList(topic.keywords) + "</div></div>";
      }
      if (topic.dunders && topic.dunders.length) {
        html += '<div class="meta-block"><h3>Special methods</h3><div class="badges">' +
          badgeList(topic.dunders, "dunder") + "</div></div>";
      }
      if (topic.modules && topic.modules.length) {
        html += '<div class="meta-block"><h3>Modules</h3><div class="badges">' +
          badgeList(topic.modules, "module") + "</div></div>";
      }
      html += "</div>";
    }

    if (topic.note) {
      html += '<div class="note">' + escapeHtml(topic.note) + "</div>";
    }

    detailEl.innerHTML = html;
    document.getElementById("main").scrollTop = 0;
  }

  function selectTopic(index) {
    currentIndex = index;
    renderList();
    renderDetail(TOPICS[index]);
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
      const haystack = (topic.title + " " + topic.sub + " " + (topic.keywords || []).join(" ") +
        " " + (topic.modules || []).join(" ")).toLowerCase();
      li.classList.toggle("hidden", q.length > 0 && !haystack.includes(q));
    });
  }

  searchEl.addEventListener("input", (e) => filterList(e.target.value));

  navToggle.addEventListener("click", () => {
    const open = sidebarEl.classList.toggle("open");
    navToggle.setAttribute("aria-expanded", open ? "true" : "false");
  });

  document.addEventListener("keydown", (e) => {
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
