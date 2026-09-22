# Python Training

A 14-stage Python training program: exercises, reference solutions, an
automated test runner (CLI + GUI), and an in-editor reference presentation.

## Structure

```
PythonTraining/
├── exercises/            One folder per stage, one subfolder per exercise --
│   └── stageNN/            trainees edit each exercise's own solution.py.
│       ├── README.md      Stage overview + list of that stage's exercises
│       └── exerciseXX/
│           ├── README.md    That exercise's own problem statement
│           └── solution.py  Stub with signatures + docstrings, raises
│                            NotImplementedError until filled in. No
│                            `if __name__ == "__main__":` block by design --
│                            this stays a plain importable module. Add a
│                            helper submodule (e.g. helpers.py) right next
│                            to it if you want to split your solution up --
│                            solution.py just has to stay the entry point.
├── reference_solutions/  Fully worked answer key, mirroring exercises/'s
│   └── stageNN/             stageNN/exerciseXX/ layout exactly -- not
│       └── exerciseXX/      visible to trainees during the course.
│           └── solution.py
│   ├── challenges/        Worked answers for challenges/, same idea.
│   │   └── challengeNN/solution.py
│   └── exams/             Worked answers for exams/, same idea.
│       └── examNN/solution.py
├── tests/                 Staff-authored pytest files, one per EXERCISE --
│   ├── test_stageNN_exerciseXX.py  each exercise is independently testable
│   ├── test_challengeNN.py         and its own git-hook target (plus one
│   └── test_examNN.py              file per challenge, one per exam). Kept
│                          separate from exercises/, challenges/, and
│                          exams/ so trainees can't edit the tests
│                          themselves.
├── challenges/            26 interview-style coding challenges (two per
│   └── challengeNN/        stage, Stages 1-13), each an integration problem
│       ├── README.md        pulling in many of that stage's topics at
│       └── solution.py      once. See challenges/README.md for details.
├── exams/                 3 evaluation exams, each integrating as much
│   └── examNN/              material as possible from a whole RUN of
│       ├── README.md        stages (not just one). See exams/README.md
│       └── solution.py      for details.
├── tools/                 The test runner (see below).
│   ├── core.py             Shared logic
│   ├── cli.py              Command-line interface
│   ├── gui.py               Tkinter GUI
│   ├── install-git-hooks.bat  Installs the pre-commit/pre-push hooks (Windows)
│   └── install-git-hooks.sh    same, for macOS/Linux
├── .githooks/             Tracked hook scripts the installers point git at
│   ├── pre-commit           (git config core.hooksPath .githooks).
│   ├── pre-push               pre-commit is always per-exercise; pre-push
│   └── run-tests-for-changed-files.sh  defaults to per-exercise too but is
│                          configurable -- see "Git hook integration".
├── presentation/          Open presentation/index.html in a browser.
│                          Topic reference (documentation-grade prose,
│                          keywords, dunders, modules, a clickable "day
│                          guide" deep dive per schedule day, book/web
│                          references) -- no graded exercises. Keep it
│                          open in a second window/monitor next to your
│                          editor and terminal.
│   ├── data.js              Topics, schedules, tier text, challenges
│   ├── glossary.js          One entry per clickable badge
│   ├── dayguides.js         Day-guide deep dives (2 verified examples each)
│   ├── highlight.js         Dependency-free VS Code-style syntax highlighter
│   └── script.js / style.css
├── conftest.py            Makes `from exercises.stageNN.exerciseXX.solution
│                          import ...` work from pytest (plain implicit
│                          namespace packages, no __init__.py anywhere).
├── requirements.txt
└── generate.py            Re-generates exercises/, reference_solutions/,
                           and tests/ from scratch if you ever need to reset
                           the starter state -- orchestrates the per-stage
                           content modules in generator/stageNN.py (this does
                           NOT touch anything a trainee has already written
                           unless you run it).
```

Every stage's exercises are designed so that every keyword, builtin, dunder,
stdlib module, and named concept from that stage's presentation topic
(`presentation/data.js`) gets exercised by the trainee's own code in **at
least three separate places** within that stage -- not just demonstrated
once and moved past. That's why most stages have five to eight exercises
instead of one: the extra exercises exist specifically to revisit the same
handful of constructs from a different angle, not to introduce new scope.
Stage 14 (Capstone) is the one exception -- see `generator/stage14.py` for
why.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Running tests

Trainees don't need to know pytest syntax until Stage 11 -- that's the whole
point of the GUI. Both tools call the same underlying test-running code
(`tools/core.py`), so they always behave identically.

**CLI** (from the repo root):
```bash
python tools/cli.py list                    # see all 14 stages, their exercises, 26 challenges, + 3 exams
python tools/cli.py test stage01             # run every exercise in one stage
python tools/cli.py test stage01_exercise03  # run just that one exercise
python tools/cli.py test challenge01        # run one interview challenge
python tools/cli.py test exam01             # run one evaluation exam
python tools/cli.py test --all              # run everything (stages + challenges + exams)
```

**GUI** (from the repo root):
```bash
python tools/gui.py
```
Pick a stage from the dropdown, click "Run Tests", read the colored
pass/fail output. No command-line knowledge required. The GUI's dropdown
is stages-only -- run challenge tests from the CLI (`test challengeNN`) or
let a `test --all` pick them up.

## Git hook integration

A ready-to-run pre-commit + pre-push hook is included:

- **pre-commit** looks at which `exercises/stageNN/exerciseXX/*.py` files
  (`solution.py` itself, or a helper submodule you added next to it),
  `exams/examNN/solution.py`, or `challenges/challengeNN/solution.py`
  files are staged, maps each one to its own exercise/exam/challenge id,
  and runs `python tools/cli.py test <id>` for **only** that one --
  `stage01_exercise03`, not all of `stage01`. Fast, focused feedback on
  exactly what you just changed. Always this granularity, not
  configurable.
- **pre-push** does the same mapping over whatever changed between the
  remote ref and what's being pushed, re-checking pre-commit's job on
  what's actually about to leave your machine (so a commit made with
  `--no-verify`, or anything else that slipped past pre-commit, still
  gets caught before it ships) -- but **its granularity is configurable**,
  since pushing per exercise is the common case:

  ```bash
  git config hooks.pushGranularity exercise   # default -- just the exercise(s)/exam(s)/challenge(s) that changed
  git config hooks.pushGranularity stage      # every exercise in any stage touched, not just the one(s) that changed
  git config --unset hooks.pushGranularity    # back to the default (exercise)
  ```

  `stage` is deliberately broader: it catches a stage left inconsistent
  by commits made with `--no-verify`, or an earlier exercise a later
  change in the same stage accidentally broke -- useful if you're about
  to push a whole stage's worth of commits at once instead of one
  exercise at a time. An exam or challenge always tests as just itself
  either way (neither is split into smaller units, so there's no wider
  target to expand `stage` to). An unset or unrecognized value falls
  back to `exercise` with a warning, never a hard failure.

Neither hook runs the full suite or `test --all`. A commit or push that
doesn't touch any exercise/exam/challenge file (docs, tests, the
presentation, anything else) passes straight through untested, since
there's nothing new to check. Install it once per local clone:

```bash
tools\install-git-hooks.bat     # Windows
sh tools/install-git-hooks.sh   # macOS/Linux
```

This points git at the tracked `.githooks/` folder (`git config
core.hooksPath .githooks`) instead of copying files into the untracked
`.git/hooks/`, so the hooks stay in sync with the repo automatically.
The matching logic lives in `.githooks/run-tests-for-changed-files.sh`,
shared by both hooks -- it reads changed file paths from stdin and an
optional `exercise`/`stage` argument (defaulting to `exercise`), and maps
each changed file to its test id at that granularity. Skip a single
check when you need to with `git commit --no-verify` /
`git push --no-verify`.

Because only *staged*/*pushed* exercises get tested (plus, at `stage`
granularity, only stages you actually touched), this is safe to install
both in a trainee's own working copy as they fill in `exercises/` stage
by stage, and on this template repo itself: editing an unrelated file
(like this README) is never blocked by some other exercise's stub still
raising `NotImplementedError`. It only blocks a commit or push when the
specific exercise/exam/challenge you just changed (or, at `stage`
granularity on push, any exercise in a stage you touched) doesn't pass
its own tests yet.

See `tests/test_stage12_exercise*.py` and `tests/test_stage13_exercise*.py`
for the two exceptions that need special handling if you extend this
further:

- **Stage 12 (requests + threading):** every test mocks `requests.get`/
  `requests.post` -- never point a hook at a live endpoint.
- **Stage 13 (FastAPI):** every test uses `fastapi.testclient.TestClient`,
  which calls the app in-process. No real server or port needed.

## Presentation

`presentation/index.html` is a standalone, dependency-free reference (no
CDN, no build step, no internet required) covering all 14 topics at
Basic / Mid / Advanced tiers, plus a "Python internals" explanation for
each one, book and web references, and six badge groups: keywords &
syntax, methods & attributes, special methods (dunders), modules,
concepts, and theory. It intentionally contains no exercises or
answers -- it's meant to sit open next to your terminal and editor as a
lookup tool, matching the actual working environment (cmd + VS Code)
the course is delivered in.

Every tier's explanation (`basic`/`mid`/`advanced` in `presentation/data.js`)
is written as full explanatory prose, not a bare list of keywords -- each
one covers what a concept is, why it matters, and how to actually use it,
so the reference doubles as documentation a trainer can teach straight
from and a student can self-study from without anyone standing over their
shoulder to fill in the gaps.

Each of the 14 topics also opens with a **stage schedule**: five
day-by-day rows (`schedule` in `presentation/data.js`) naming what to
cover each day so a stage maps onto a standard 5-day training stage. Day
1 of Stage 1 (Python Fundamentals) is reserved entirely for environment
setup -- installing Python, creating the virtual environment, running
`tools/cli.py` for the first time, and touring the repo -- so no actual
topic content is taught that day; every other stage's five days split
across basic tier, mid tier, advanced tier + internals, exercises, and
a practice/review day. Stage 14 (Capstone) uses a project-shaped
schedule (kickoff, build, build, polish, demo) instead of tiers, since
it has no new content of its own.

Click any badge to open a glossary drawer (docked to the right, non-modal --
the sidebar and content stay fully usable while it's open) with a full
explanation, when/how to use it, and a runnable example -- entries are
defined in `presentation/glossary.js`, keyed by the exact badge text used
in `presentation/data.js`. Adding a new badge to a topic means adding a
matching entry there too.

The **Stage schedule** table itself is also clickable: every Basic/Mid/
Advanced-tier day (not the setup/exercises/review days, which have no new
topic content) opens the same drawer with a "day guide" -- a deeper dive
than the tier prose above it, built around runnable examples rather than
more explanation. Each one has at least two examples, every example shown
with real VS Code Dark+-style syntax highlighting (a small dependency-free
tokenizer in `presentation/highlight.js` -- still no CDN) and its actual,
executed output underneath, not a hand-typed guess. This content lives in
`presentation/dayguides.js`, keyed by `stageNN-basic` / `-mid` / `-advanced`
to match each schedule row's `guideKey`. The single-example code blocks in
the regular glossary drawer are syntax-highlighted the same way.

Every one of the first 13 topics also shows two **Interview Challenge**
callouts each -- pointers to the interview-style problems in `challenges/`,
described below.

There's also a 15th topic, "Appendix: The Tooling Itself", covering
argparse, subprocess, tkinter, ANSI terminal colors, virtual
environments, and git hooks -- everything used to build `tools/cli.py`,
`tools/gui.py`, and `tools/core.py` themselves, so a trainee who works
through the whole reference has what they need to build a similar
CLI+GUI test runner from scratch.

Open `presentation/index.html` directly in any browser.

## Interview Challenges

`challenges/` holds 26 standalone, interview-style coding problems -- two
for every stage that has its own topic list (Stages 1-13) -- separate from
the graded stage exercises in `exercises/`, but tested the same way:

```bash
python tools/cli.py test challenge01       # run one challenge's tests
python tools/cli.py test --all             # runs every stage's AND every challenge's tests
```

Each one is the kind of problem an engineer actually gets asked to write
live in a technical interview: more code than a stage exercise, and a
real specification instead of one function signature. Unlike the stage
exercises -- which each drill one technique in isolation -- every
challenge is deliberately built to pull in *as many* of its stage's
keywords, dunders, modules, methods, and concepts as it can, so it's an
integration problem, not a single-topic snippet; expect each one to take
real, focused time. A handful are straight from LeetCode (cited by number
below); the rest are original, realistic tasks in the same spirit.
`tests/test_challengeNN.py` grades correctness and the documented edge
cases automatically, same as a stage's exercise -- but each challenge's
`README.md` also imposes explicit constraints on *how* to write the
solution (a required technique, a forbidden shortcut, or a mandated
interface), which pytest can't check. Grade those by reading the code.

| Challenge | Title | LeetCode | Do it after |
|---|---|---|---|
| `challenge01` | Typed Config Loader | -- | Stage 01 -- Python Fundamentals |
| `challenge02` | Identity, Equality, and a Login Prompt | -- | Stage 01 -- Python Fundamentals |
| `challenge03` | Log Stream Parser and Scanner | -- | Stage 02 -- Control Flow |
| `challenge04` | Batch Retry Simulator | -- | Stage 02 -- Control Flow |
| `challenge05` | Pluggable Event Pipeline | -- | Stage 03 -- Functions |
| `challenge06` | Streaming Metrics Aggregator | -- | Stage 03 -- Functions |
| `challenge07` | Anagram Groups with Records | #49 | Stage 04 -- Data Structures |
| `challenge08` | Longest Consecutive Run of Records | #128 | Stage 04 -- Data Structures |
| `challenge09` | Log File Parser with a Custom Exception Chain | -- | Stage 05 -- Files, Exceptions, Regex |
| `challenge10` | Log Text Utilities with a Custom Context Manager | -- | Stage 05 -- Files, Exceptions, Regex |
| `challenge11` | LRU Cache with a Descriptor and Class-Level Stats | #146 | Stage 06 -- OOP I |
| `challenge12` | Min Stack with Class-Level Push Stats | #155 | Stage 06 -- OOP I |
| `challenge13` | Notification System with Mixins and ABCs | -- | Stage 07 -- OOP II |
| `challenge14` | Shape Library with Protocols and Composition | -- | Stage 07 -- OOP II |
| `challenge15` | Matrix: A Rich Numeric Type | -- | Stage 08 -- The Python Data Model |
| `challenge16` | Transaction Ledger: Callable and Context Manager | -- | Stage 08 -- The Python Data Model |
| `challenge17` | Directory Report Builder | -- | Stage 09 -- OS, JSON, Datetime, XML |
| `challenge18` | XML Feed to Timezone-Aware Digest | -- | Stage 09 -- OS, JSON, Datetime, XML |
| `challenge19` | Sales Data Analyzer | -- | Stage 10 -- Pandas |
| `challenge20` | Two Sum, Pandas-Style, with Joins and Diagnostics | #1 | Stage 10 -- Pandas |
| `challenge21` | Document Scanner Preprocessing Pipeline | -- | Stage 11 -- OpenCV |
| `challenge22` | Face-Region Redactor | -- | Stage 11 -- OpenCV |
| `challenge23` | Rate-Limited HTTP Client | -- | Stage 12 -- Requests + Threading |
| `challenge24` | Bounded Job Queue with Retry and ThreadPoolExecutor | -- | Stage 12 -- Requests + Threading |
| `challenge25` | URL Shortener API with Dependency-Injected Auth | -- | Stage 13 -- FastAPI |
| `challenge26` | Underground System API with Live Diagnostics | #1396 | Stage 13 -- FastAPI |

See `challenges/README.md` for the full picture, and each
`challenges/challengeNN/README.md` for that problem's statement and
constraints. Worked answers are in `reference_solutions/challenges/`,
verified against the same tests before being committed.

## Evaluation Exams

`exams/` holds 3 checkpoint exams, each covering a whole **run** of
consecutive stages instead of just one:

```bash
python tools/cli.py test exam01    # run one exam's tests
python tools/cli.py test --all     # runs every stage's, challenge's, AND exam's tests
```

| Exam | Title | Covers |
|---|---|---|
| `exam01` | Order Processing Pipeline | Stages 1-4 |
| `exam02` | Document Archive System | Stages 5-9 |
| `exam03` | Product Analytics & Photo Pipeline API | Stages 10-13 |

Where a challenge integrates one stage's material, an exam integrates a
whole run of them into one connected system -- proof you can still
combine everything from stages you finished a while back, not just the
one you're currently on. Unlike the interview challenges (explicitly
optional), an exam is a checkpoint on the stages it covers; it's still
not required to move on, but it's not "not-must-to" either. See
`exams/README.md` for the full picture, and each `exams/examNN/README.md`
for that exam's problem statement. Worked answers are in
`reference_solutions/exams/`, verified against the same tests before
being committed.

## Progress Reports

Each student works on their own branch, named `<group>/<user_id>` --
e.g. `group1/orgutier` (`group1` here is just whatever label you use to
tell one cohort/section apart from another; `orgutier` is the student's
own identifier, typically their GitHub username). `tools/report.py`
fetches every branch matching that shape, grades each one, and writes
the results into a single `report.xlsx` you can hand to shareholders:

```bash
python tools/report.py                                        # fetch + grade every group/user_id branch on origin
python tools/report.py --pattern "cohort2025-*/*"              # only that cohort's branches
python tools/report.py --output cohort2025.xlsx --workers 8    # faster, custom filename
python tools/report.py --local                                 # grade branches you already have locally, skip fetching
```

The output workbook has four sheets:

- **Summary** -- one row per student (Group, User, Branch, exercises
  solved/total/%, challenges solved/total/%, exams solved/total/%,
  Status), color-scaled so the weakest and strongest students stand out
  at a glance.
- **Exercises** -- one row per student, one column per exercise, grouped
  under a merged "Stage NN" header, with a class-wide "Solved by" count
  along the bottom of each column.
- **Challenges** -- the same shape, for the (optional, not-must-do)
  interview challenges, kept on its own sheet so it never gets averaged
  into the required exercise total.
- **Exams** -- one column per evaluation exam (each labeled with the
  stage range it covers), also kept on its own sheet -- an exam is a
  checkpoint, not an optional extra like a challenge, so it isn't
  averaged into either of the other two totals either.

For each matching branch, the script checks it out into a throwaway `git
worktree` (your own working copy is never touched), overlays **this
checkout's own `tests/` and `conftest.py`** on top of the student's
`exercises/`/`challenges/`/`exams/` trees, and runs every exercise's,
challenge's, and exam's own test file against it -- a student's branch
is graded by the current, canonical test suite, never by whatever copy
of `tests/` happens to be sitting in their own branch (they're not
supposed to edit it, but this makes sure a stale or modified copy can't
skew their grade either way). A branch that predates some
exercise/challenge/exam (e.g. it was created before Stage 14 existed)
simply doesn't have that folder yet, so it's counted as not solved --
this reports what currently passes, not intent or timing.

By default it excludes `main`, `master`, `HEAD`, and a few common
non-student prefixes (`claude/*`, `dependabot/*`, `renovate/*`,
`gh-pages`) so it's safe to run with no arguments even against this
template repo's own branches; scope `--pattern` to your actual group
keyword(s) for a large, busy repo. Grading ~100 exercises/challenges/exams
takes roughly 20-30 seconds per student sequentially -- `--workers` (a
handful of branches at a time is a reasonable default) parallelizes
across students, each in its own worktree.

## On book references

Every topic's reference prioritizes *Python Distilled* and *Fluent Python*.
Where neither covers a topic (mainly the third-party libraries: pandas,
OpenCV, requests, FastAPI), the reference points to that library's own
official documentation instead. Two topics have an optional third-book
candidate noted in the presentation and in
`reference_solutions` planning notes -- pandas (*Python for Data Analysis*,
Wes McKinney) and OpenCV (*Practical Python and OpenCV*, Adrian Rosebrock).
Neither is required; the official docs cover this course's scope on their
own. Add either only if you want to.
