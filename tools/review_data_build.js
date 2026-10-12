/*
 * Step 2 of regenerating presentation-review/reviewdata.js.
 *
 * Loads presentation/data.js's TOPICS (the single source of truth for each
 * stage's tier-level keywords/dunders/modules/methods/concepts/theory + book
 * ref) plus the JSON dumped by review_data_extract.py, walks the whole
 * course in order, and works out -- for every tier, every individual
 * exercise, every interview challenge, and every exam -- which tagged terms
 * are being introduced for the FIRST time ("New") versus reappearing
 * ("Refresh"). Writes presentation-review/reviewdata.js.
 *
 * Usage (from the repo root):
 *   python tools/review_data_extract.py /tmp/review_extract
 *   node tools/review_data_build.js /tmp/review_extract
 */
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const inputDir = process.argv[2];
if (!inputDir) {
  console.error("Usage: node tools/review_data_build.js <extract_dir>");
  process.exit(1);
}

// ---- load presentation/data.js's TOPICS -----------------------------------
const dataJsSrc = fs.readFileSync(path.join(ROOT, "presentation/data.js"), "utf8");
const TOPICS = new Function(dataJsSrc + "; return TOPICS;")();
const topicByN = {};
TOPICS.forEach((t) => { topicByN[t.n] = t; });

// ---- load extracted exercise / challenge / exam text -----------------------
const exercisesByStage = JSON.parse(fs.readFileSync(path.join(inputDir, "exercises.json"), "utf8"));
const { challenges: challengeData, exams: examData } = JSON.parse(fs.readFileSync(path.join(inputDir, "challenges_exams.json"), "utf8"));

// ---- matching helpers -------------------------------------------------------
// A handful of tags are syntax PATTERNS rather than literal tokens (e.g. "a
// class statement with a base class"), so they get their own regex instead
// of the generic bare-identifier / substring rule below.
const SPECIAL_PATTERNS = {
  "class Child(Parent)": /class\s+\w+\s*\(\s*[A-Za-z_]/,
  "x: int = 5": /\b\w+\s*:\s*\w+(\[[^\]]*\])?\s*=/,
  "[x for x in ...]": /\[[^\[\]]*\bfor\b[^\[\]]*\bin\b[^\[\]]*\]/,
  "{k:v for ...}": /\{[^{}]*\bfor\b[^{}]*\bin\b[^{}]*\}/,
};

function isBareIdentifier(s) {
  return /^[A-Za-z_][A-Za-z0-9_]*$/.test(s);
}

function variantPresent(variant, text) {
  let v = variant.trim();
  if (!v) return false;
  v = v.replace(/^@/, "");
  v = v.replace(/\(\)$/, "");
  if (isBareIdentifier(v)) {
    // Word-boundary match so e.g. the `in` keyword doesn't match inside
    // `isinstance`, and so it's only checked against actual code (never
    // prose -- see below), where a bare `is`/`in`/`or`/`not` reliably means
    // the Python keyword rather than an English word.
    const re = new RegExp("\\b" + v.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + "\\b");
    return re.test(text);
  }
  if (v.includes(".")) {
    // A dotted tag like "df.groupby()" is usually written with SOME
    // placeholder variable name ("df") that a real solution won't
    // necessarily use -- also accept a bare ".groupby(" match so a
    // differently-named variable still counts.
    const lastSeg = v.split(".").pop();
    if (text.includes(v)) return true;
    if (lastSeg && text.includes("." + lastSeg + "(")) return true;
    if (lastSeg && text.includes("." + lastSeg)) return true;
    return false;
  }
  return text.includes(v);
}

function tagPresent(tag, text) {
  const clean = tag.replace(" (preview)", "").trim();
  if (SPECIAL_PATTERNS[clean]) return SPECIAL_PATTERNS[clean].test(text);
  const variants = clean.split("/");
  return variants.some((v) => variantPresent(v, text));
}

// ---- glossary categories ----------------------------------------------------
const CATS = ["keywords", "dunders", "modules", "methods", "concepts", "theory"];
// Code-detectable categories only, used for exercise/challenge/exam
// auto-detection -- concepts/theory are abstract and aren't literal code
// tokens, so they're only ever tracked at the tier level.
const CODE_CATS = ["keywords", "dunders", "modules", "methods"];

// ---- hand-authored Testing-tier (tier4_testing, stages 1-7) ----------------
// Not tagged in the original presentation/data.js (its schedule tiers only
// have Basic/Mid/Advanced) -- this page's own addition, kept consistent
// across all 7 stages since it's deliberately the SAME skill practiced
// repeatedly (which is exactly why stage02-07's occurrence should show as
// Refresh, not New). Matching glossary.js entries exist for each concept
// below.
const TESTING_TIER_TEMPLATE = {
  label: "Testing tier",
  keywords: [],
  dunders: [],
  modules: [],
  methods: [],
  concepts: ["manual test verification (no framework)", "expected-vs-actual comparison", "test oracle"],
  theory: [],
  ref: "Web — Python docs, unittest module overview (docs.python.org/3/library/unittest.html) -- read for how a real framework formalizes exactly the checks you just wrote by hand",
};

// tier0 (Setup, stage01 only) -- ad hoc, from tier0_hello_world's own summary.
const TIER0_TEMPLATE = {
  label: "Setup",
  keywords: ["print()"],
  dunders: [],
  modules: [],
  methods: [],
  concepts: ["variable assignment", "string concatenation"],
  theory: [],
  ref: "Book — Python Distilled, §1.1–1.3 (a first program, variables, strings)",
};

function emptyBuckets() {
  const o = {};
  CATS.forEach((c) => (o[c] = []));
  return o;
}

// =============================================================================
// Course-ordered walk building the cumulative "seen" set, tier by tier.
// =============================================================================
const seen = new Set(); // every keyword/dunder/module/method/concept/theory string seen so far
const seenCode = new Set(); // subset restricted to CODE_CATS, used for exercise/challenge/exam detection

const stagesOut = [];

function tierFromSchedule(stageTopic, tierIndex) {
  // Stage 1 has an extra "Setup" step before "Learn" in its schedule array
  // (the other stages don't), so find the step that actually carries
  // `tiers` instead of assuming a fixed index.
  const learnStep = (stageTopic.schedule || []).find((s) => s.tiers);
  const tiers = learnStep && learnStep.tiers;
  return (tiers && tiers[tierIndex]) || {};
}

function refFor(stageTopic, tierIndex) {
  const key = ["basic", "mid", "advanced"][tierIndex];
  return (stageTopic[key] && stageTopic[key].ref) || "";
}

function buildTierEntry(rawTier, ref, exerciseList) {
  const newB = emptyBuckets();
  const refreshB = emptyBuckets();
  CATS.forEach((cat) => {
    (rawTier[cat] || []).forEach((term) => {
      if (seen.has(term)) refreshB[cat].push(term);
      else { newB[cat].push(term); seen.add(term); }
      if (CODE_CATS.includes(cat)) seenCode.add(term);
    });
  });

  const hasNew = CATS.some((c) => newB[c].length);
  const newCodeTerms = [];
  CODE_CATS.forEach((c) => newB[c].forEach((t) => newCodeTerms.push({ term: t, cat: c })));

  // Attribute each new, code-detectable term to the specific exercise(s) in
  // this tier whose own reference solution actually uses it. A term neither
  // exercise's code literally uses (introduced by the tier's Learn material
  // rather than exercised by either specific solution) stays in
  // `tierOnlyNew` instead of being force-attributed to an exercise that
  // doesn't actually contain it.
  const exercises = exerciseList.map((ex) => {
    // Detect against the actual CODE only, never the hand-written summary
    // prose -- a summary like "// and % chained together" contains the
    // English word "and", which would otherwise falsely match the `and`
    // keyword tag.
    const text = ex.reference_solution || "";
    const exNew = emptyBuckets();
    newCodeTerms.forEach(({ term, cat }) => {
      if (tagPresent(term, text)) exNew[cat].push(term);
    });
    return { id: ex.id, name: ex.name, title: ex.title, summary: ex.summary, newItems: exNew };
  });

  const tierOnlyNew = emptyBuckets();
  CODE_CATS.forEach((cat) => {
    newB[cat].forEach((term) => {
      const already = exercises.some((e) => e.newItems[cat].includes(term));
      if (!already) tierOnlyNew[cat].push(term);
    });
  });

  return {
    label: rawTier.label,
    ref: hasNew ? ref : "",
    newItems: newB,
    refreshItems: refreshB,
    tierOnlyNew,
    exercises,
  };
}

for (let n = 1; n <= 13; n++) {
  const stageTopic = topicByN[n];
  const stageId = "stage" + String(n).padStart(2, "0");
  const exList = exercisesByStage[stageId];
  const byName = {};
  exList.forEach((e) => (byName[e.name] = e));

  const tiers = [];

  if (n === 1) {
    tiers.push(buildTierEntry(TIER0_TEMPLATE, TIER0_TEMPLATE.ref, [byName["tier0_hello_world"]]));
  }

  const tierSpecs = [
    { idx: 0, names: ["tier1_basic01", "tier1_basic02"] },
    { idx: 1, names: ["tier2_mid01", "tier2_mid02"] },
    { idx: 2, names: ["tier3_advanced01", "tier3_advanced02"] },
  ];
  tierSpecs.forEach((spec) => {
    const rawTier = tierFromSchedule(stageTopic, spec.idx);
    const ref = refFor(stageTopic, spec.idx);
    const list = spec.names.map((nm) => byName[nm]).filter(Boolean);
    tiers.push(buildTierEntry(rawTier, ref, list));
  });

  if (byName["tier4_testing"]) {
    tiers.push(buildTierEntry(TESTING_TIER_TEMPLATE, TESTING_TIER_TEMPLATE.ref, [byName["tier4_testing"]]));
  }

  stagesOut.push({ n, title: stageTopic.title, sub: stageTopic.sub, tiers });
}

// ---- Stage 14 Capstone: synthesis, essentially no new material ------------
{
  const stageTopic = topicByN[14];
  stagesOut.push({
    n: 14,
    title: stageTopic.title,
    sub: stageTopic.sub,
    isCapstone: true,
    newConcepts: stageTopic.concepts || [],
    note: (stageTopic.basic && stageTopic.basic.text) || "",
  });
}

// =============================================================================
// Challenges -- grouped by owning stage. By design (see challenges/README.md
// and each challenge's own "Do this after: Stage NN" line), a challenge only
// ever draws on tools its own stage (or an earlier one) already introduced --
// it's practice, not new material -- so every tag a challenge's reference
// solution touches is shown as Refresh, never New.
// =============================================================================
const challengesOut = {};
for (let cn = 1; cn <= 26; cn++) {
  const cid = "challenge" + String(cn).padStart(2, "0");
  const info = challengeData[cid];
  if (!info) continue;
  const stageTopic = topicByN[parseInt(info.stage.replace("stage", ""), 10)];
  const meta = (stageTopic.challenges || []).find((c) => c.id === cid) || {};
  // Same reasoning as exercises: detect against the reference solution's
  // actual code, never the hand-written blurb prose.
  const text = info.solution || "";
  challengesOut[cid] = { id: cid, title: meta.title || "", blurb: meta.blurb || "", stage: info.stage, _text: text };
}

// The per-category rescan needs the category each seen term belongs to;
// rebuild that map once from everything emitted in stagesOut.
const termCategory = {};
stagesOut.forEach((s) => {
  if (s.isCapstone) return;
  s.tiers.forEach((t) => {
    CODE_CATS.forEach((cat) => {
      (t.newItems[cat] || []).forEach((term) => (termCategory[term] = cat));
      (t.refreshItems[cat] || []).forEach((term) => (termCategory[term] = cat));
    });
  });
});

Object.keys(challengesOut).forEach((cid) => {
  const c = challengesOut[cid];
  const refreshB = emptyBuckets();
  seenCode.forEach((term) => {
    if (!tagPresent(term, c._text)) return;
    const cat = termCategory[term] || "keywords";
    refreshB[cat].push(term);
  });
  c.newItems = emptyBuckets();
  c.refreshItems = refreshB;
  delete c._text;
});

// =============================================================================
// Exams -- pure review across the stage range they cover.
// =============================================================================
const examsOut = {};
Object.keys(examData).forEach((eid) => {
  const info = examData[eid];
  const text = info.solution || "";
  const refreshB = emptyBuckets();
  seenCode.forEach((term) => {
    if (!tagPresent(term, text)) return;
    const cat = termCategory[term] || "keywords";
    refreshB[cat].push(term);
  });
  examsOut[eid] = { id: eid, lo: info.lo, hi: info.hi, refreshItems: refreshB };
});

// =============================================================================
const OUT = { stages: stagesOut, challenges: challengesOut, exams: examsOut };
const outPath = path.join(ROOT, "presentation-review", "reviewdata.js");
const header =
  "// Auto-generated -- see tools/review_data_extract.py + tools/review_data_build.js.\n" +
  "// Regenerate rather than hand-edit if exercises/challenges/exams/data.js change:\n" +
  "//   python tools/review_data_extract.py /tmp/review_extract\n" +
  "//   node tools/review_data_build.js /tmp/review_extract\n";
fs.writeFileSync(outPath, header + "const REVIEW_DATA = " + JSON.stringify(OUT, null, 1) + ";\n");
console.log("Wrote", outPath);
console.log("stages:", stagesOut.length, "challenges:", Object.keys(challengesOut).length, "exams:", Object.keys(examsOut).length);
