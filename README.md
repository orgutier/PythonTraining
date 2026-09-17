# Python Training

A 14-week Python training program: exercises, reference solutions, an
automated test runner (CLI + GUI), and an in-editor reference presentation.

## Structure

```
PythonTraining/
├── exercises/            One folder per week. Trainees edit solution.py here.
│   └── weekNN/
│       ├── README.md      Exercise description
│       └── solution.py    Stub with signatures + docstrings, raises
│                          NotImplementedError until filled in. No
│                          `if __name__ == "__main__":` block by design --
│                          this stays a plain importable module.
├── reference_solutions/  Fully worked answer key, one folder per week --
│   └── weekNN/            not visible to trainees during the course.
│       └── solution.py
├── tests/                 Staff-authored pytest files, one per week.
│   └── test_weekNN.py     Kept separate from exercises/ so trainees can't
│                          edit the tests themselves.
├── tools/                 The test runner (see below).
│   ├── core.py             Shared logic
│   ├── cli.py              Command-line interface
│   └── gui.py               Tkinter GUI
├── presentation/          Open presentation/index.html in a browser.
│                          Topic reference only (theory, keywords, dunders,
│                          modules, book/web references) -- no exercises.
│                          Keep it open in a second window/monitor next to
│                          your editor and terminal.
├── conftest.py            Makes `from exercises.weekNN.solution import ...`
│                          work from pytest.
├── requirements.txt
└── generate.py            Re-generates exercises/, reference_solutions/,
                           and tests/ from scratch if you ever need to reset
                           the starter state (this does NOT touch anything
                           a trainee has already written unless you run it).
```

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
python tools/cli.py list              # see all 14 weeks
python tools/cli.py test week01       # run one week
python tools/cli.py test --all        # run everything
```

**GUI** (from the repo root):
```bash
python tools/gui.py
```
Pick a week from the dropdown, click "Run Tests", read the colored
pass/fail output. No command-line knowledge required.

## Git hook integration

If you're wiring this into a git hook that auto-tests on commit: detect
which `exercises/weekNN/` changed in the commit, then run
`python tools/cli.py test weekNN` (or import `tools/core.py` directly) and
gate the commit on the exit code. See `tests/test_week12.py` and
`tests/test_week13.py` for the two exceptions that need special handling:

- **Week 12 (requests + threading):** the test mocks `requests.get` --
  never point a hook at the live `jsonplaceholder.typicode.com` endpoint.
- **Week 13 (FastAPI):** the test uses `fastapi.testclient.TestClient`,
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

Click any badge to open a glossary drawer (docked to the left, next to
the topic list) with a full explanation, when/how to use it, and a
runnable example -- entries are defined in `presentation/glossary.js`,
keyed by the exact badge text used in `presentation/data.js`. Adding a
new badge to a topic means adding a matching entry there too.

There's also a 15th topic, "Appendix: The Tooling Itself", covering
argparse, subprocess, tkinter, ANSI terminal colors, virtual
environments, and git hooks -- everything used to build `tools/cli.py`,
`tools/gui.py`, and `tools/core.py` themselves, so a trainee who works
through the whole reference has what they need to build a similar
CLI+GUI test runner from scratch.

Open `presentation/index.html` directly in any browser.

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
