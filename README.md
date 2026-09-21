# Python Training

A 14-week Python training program: exercises, reference solutions, an
automated test runner (CLI + GUI), and an in-editor reference presentation.

## Structure

```
PythonTraining/
├── exercises/            One folder per week, one subfolder per exercise --
│   └── weekNN/            trainees edit each exercise's own solution.py.
│       ├── README.md      Week overview + list of that week's exercises
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
│   └── weekNN/             weekNN/exerciseXX/ layout exactly -- not
│       └── exerciseXX/      visible to trainees during the course.
│           └── solution.py
│   └── challenges/        Worked answers for challenges/, same idea.
│       └── challengeNN/solution.py
├── tests/                 Staff-authored pytest files, one per EXERCISE --
│   ├── test_weekNN_exerciseXX.py  each exercise is independently testable
│   └── test_challengeNN.py         and its own git-hook target (plus one
│                          file per challenge). Kept separate from
│                          exercises/ and challenges/ so trainees can't
│                          edit the tests themselves.
├── challenges/            10 interview-style coding challenges (two per
│   └── challengeNN/        assigned week), separate from the graded
│       ├── README.md        weekly exercises but tested the same way.
│       └── solution.py      See challenges/README.md for what these are.
├── tools/                 The test runner (see below).
│   ├── core.py             Shared logic
│   ├── cli.py              Command-line interface
│   ├── gui.py               Tkinter GUI
│   ├── install-git-hooks.bat  Installs the pre-commit/pre-push hooks (Windows)
│   └── install-git-hooks.sh    same, for macOS/Linux
├── .githooks/             Tracked hook scripts the installers point git at
│   ├── pre-commit           (git config core.hooksPath .githooks).
│   ├── pre-push              pre-commit tests just the exercise(s) staged;
│   └── run-tests-for-changed-files.sh  pre-push tests the whole week for
│                          any exercise touched -- see "Git hook integration".
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
├── conftest.py            Makes `from exercises.weekNN.exerciseXX.solution
│                          import ...` work from pytest (plain implicit
│                          namespace packages, no __init__.py anywhere).
├── requirements.txt
└── generate.py            Re-generates exercises/, reference_solutions/,
                           and tests/ from scratch if you ever need to reset
                           the starter state -- orchestrates the per-week
                           content modules in generator/weekNN.py (this does
                           NOT touch anything a trainee has already written
                           unless you run it).
```

Every week's exercises are designed so that every keyword, builtin, dunder,
stdlib module, and named concept from that week's presentation topic
(`presentation/data.js`) gets exercised by the trainee's own code in **at
least three separate places** within that week -- not just demonstrated
once and moved past. That's why most weeks have five to eight exercises
instead of one: the extra exercises exist specifically to revisit the same
handful of constructs from a different angle, not to introduce new scope.
Week 14 (Capstone) is the one exception -- see `generator/week14.py` for
why.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Running tests

Trainees don't need to know pytest syntax until Week 11 -- that's the whole
point of the GUI. Both tools call the same underlying test-running code
(`tools/core.py`), so they always behave identically.

**CLI** (from the repo root):
```bash
python tools/cli.py list                    # see all 14 weeks, their exercises, + 10 challenges
python tools/cli.py test week01             # run every exercise in one week
python tools/cli.py test week01_exercise03  # run just that one exercise
python tools/cli.py test challenge01        # run one interview challenge
python tools/cli.py test --all              # run everything (weeks + challenges)
```

**GUI** (from the repo root):
```bash
python tools/gui.py
```
Pick a week from the dropdown, click "Run Tests", read the colored
pass/fail output. No command-line knowledge required. The GUI's dropdown
is weeks-only -- run challenge tests from the CLI (`test challengeNN`) or
let a `test --all` pick them up.

## Git hook integration

A ready-to-run pre-commit + pre-push hook is included, and the two are
**deliberately different granularities**, not the same check run twice:

- **pre-commit is atomic, per exercise.** It looks at which
  `exercises/weekNN/exerciseXX/*.py` files (`solution.py` itself, or a
  helper submodule you added next to it) or `challenges/challengeNN/solution.py`
  files are staged, maps each one to its own exercise/challenge id, and
  runs `python tools/cli.py test <id>` for **only** that exercise --
  `week01_exercise03`, not all of `week01`. Fast, focused feedback on
  exactly what you just changed.
- **pre-push tests the whole week.** For the same kind of changed files
  (this time, differing from the remote), it maps each one back to its
  **week** id and runs every exercise in that week -- `week01`, covering
  `week01_exercise01` through however many exercises that week has. This
  is deliberately broader than pre-commit: it catches a week left
  inconsistent by commits made with `--no-verify`, or an earlier exercise
  a later change in the same week accidentally broke, before any of it
  leaves your machine.

Neither runs the full suite or `test --all`, and a challenge always tests
as just itself at both stages (challenges aren't split into exercises,
so there's no larger unit to widen to). A commit or push that doesn't
touch any exercise/challenge file (docs, tests, the presentation,
anything else) passes straight through untested at either stage, since
there's nothing new to check. Install it once per local clone:

```bash
tools\install-git-hooks.bat     # Windows
sh tools/install-git-hooks.sh   # macOS/Linux
```

This points git at the tracked `.githooks/` folder (`git config
core.hooksPath .githooks`) instead of copying files into the untracked
`.git/hooks/`, so the hooks stay in sync with the repo automatically.
The matching logic lives in `.githooks/run-tests-for-changed-files.sh`,
shared by both hooks -- it takes `exercise` or `week` as an argument to
pick which granularity to map changed files to; `pre-commit` passes
`exercise`, `pre-push` passes `week`. Skip a single check when you need
to with `git commit --no-verify` / `git push --no-verify`.

Because only *staged*/*pushed* exercises get tested, this is safe to
install both in a trainee's own working copy as they fill in
`exercises/` week by week, and on this template repo itself: editing an
unrelated file (like this README) is never blocked by some other
exercise's stub still raising `NotImplementedError`. It only blocks a
commit when the specific exercise you just changed doesn't pass its own
tests yet, or a push when any exercise in a week you touched doesn't.

See `tests/test_week12_exercise*.py` and `tests/test_week13_exercise*.py`
for the two exceptions that need special handling if you extend this
further:

- **Week 12 (requests + threading):** every test mocks `requests.get`/
  `requests.post` -- never point a hook at a live endpoint.
- **Week 13 (FastAPI):** every test uses `fastapi.testclient.TestClient`,
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

Each of the 14 topics also opens with a **week schedule**: five
day-by-day rows (`schedule` in `presentation/data.js`) naming what to
cover each day so a week maps onto a standard 5-day training week. Day
1 of Week 1 (Python Fundamentals) is reserved entirely for environment
setup -- installing Python, creating the virtual environment, running
`tools/cli.py` for the first time, and touring the repo -- so no actual
topic content is taught that day; every other week's five days split
across basic tier, mid tier, advanced tier + internals, exercises, and
a practice/review day. Week 14 (Capstone) uses a project-shaped
schedule (kickoff, build, build, polish, demo) instead of tiers, since
it has no new content of its own.

Click any badge to open a glossary drawer (docked to the right, non-modal --
the sidebar and content stay fully usable while it's open) with a full
explanation, when/how to use it, and a runnable example -- entries are
defined in `presentation/glossary.js`, keyed by the exact badge text used
in `presentation/data.js`. Adding a new badge to a topic means adding a
matching entry there too.

The **Week schedule** table itself is also clickable: every Basic/Mid/
Advanced-tier day (not the setup/exercises/review days, which have no new
topic content) opens the same drawer with a "day guide" -- a deeper dive
than the tier prose above it, built around runnable examples rather than
more explanation. Each one has at least two examples, every example shown
with real VS Code Dark+-style syntax highlighting (a small dependency-free
tokenizer in `presentation/highlight.js` -- still no CDN) and its actual,
executed output underneath, not a hand-typed guess. This content lives in
`presentation/dayguides.js`, keyed by `weekNN-basic` / `-mid` / `-advanced`
to match each schedule row's `guideKey`. The single-example code blocks in
the regular glossary drawer are syntax-highlighted the same way.

Five of the topics (Data Structures, OOP I, Pandas, Requests + Threading,
and FastAPI) also show two **Interview Challenge** callouts each -- pointers
to the interview-style problems in `challenges/`, described below.

There's also a 15th topic, "Appendix: The Tooling Itself", covering
argparse, subprocess, tkinter, ANSI terminal colors, virtual
environments, and git hooks -- everything used to build `tools/cli.py`,
`tools/gui.py`, and `tools/core.py` themselves, so a trainee who works
through the whole reference has what they need to build a similar
CLI+GUI test runner from scratch.

Open `presentation/index.html` directly in any browser.

## Interview Challenges

`challenges/` holds 10 standalone, interview-style coding problems (two
per assigned week) -- separate from the graded weekly exercises in
`exercises/`, but tested the same way:

```bash
python tools/cli.py test challenge01       # run one challenge's tests
python tools/cli.py test --all             # runs every week's AND every challenge's tests
```

Each one is the kind of problem an engineer actually gets asked to write
live in a technical interview: more code than a weekly exercise, and a
real specification instead of one function signature. Half of them are
straight from LeetCode (cited by number below); the rest are original,
realistic tasks in the same spirit. `tests/test_challengeNN.py` grades
correctness and the documented edge cases automatically, same as a
week's exercise -- but each challenge's `README.md` also imposes explicit
constraints on *how* to write the solution (a required technique, a
forbidden shortcut, or a mandated interface), which pytest can't check.
Grade those by reading the code.

| Challenge | Title | LeetCode | Do it after |
|---|---|---|---|
| `challenge01` | Group Anagrams | #49 | Week 04 -- Data Structures |
| `challenge06` | Longest Consecutive Sequence | #128 | Week 04 -- Data Structures |
| `challenge02` | LRU Cache | #146 | Week 06 -- OOP I |
| `challenge07` | Min Stack | #155 | Week 06 -- OOP I |
| `challenge03` | Sales Data Analyzer | -- | Week 10 -- Pandas |
| `challenge08` | Two Sum, Pandas-Style | #1 | Week 10 -- Pandas |
| `challenge04` | Rate Limiter (Token Bucket) | -- | Week 12 -- Requests + Threading |
| `challenge09` | Bounded Blocking Queue | #1188 | Week 12 -- Requests + Threading |
| `challenge05` | URL Shortener API | -- | Week 13 -- FastAPI |
| `challenge10` | Underground System API | #1396 | Week 13 -- FastAPI |

See `challenges/README.md` for the full picture, and each
`challenges/challengeNN/README.md` for that problem's statement and
constraints. Worked answers are in `reference_solutions/challenges/`,
verified against the same tests before being committed.

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
