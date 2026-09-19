# Interview Challenges

Five standalone, interview-style coding problems, separate from the graded
weekly exercises in `exercises/`. They exist for a different purpose:

- **Weekly exercises** (`exercises/weekNN/`) are scoped tightly to that
  week's topic and are graded automatically by `tests/test_weekNN.py` via
  `python tools/cli.py test weekNN`.
- **Challenges** (`challenges/challengeNN/`) are the kind of problem an
  engineer is actually asked to write live in a technical interview: more
  code, fewer hints, and a real specification instead of a single function
  signature. They are **not** run by pytest and **not** wired into
  `tools/cli.py` -- grade them by code review against the constraints in
  each challenge's `README.md`, not by a green checkmark.

Each `challengeNN/` folder has the same shape as a week's exercise:

```
challenges/challengeNN/
  README.md      Problem statement + specific constraints on HOW to write it
  solution.py     Stub with signatures/docstrings, raises NotImplementedError
```

with a matching worked answer in `reference_solutions/challenges/challengeNN/`.

## Where each challenge fits in the course

| Challenge | Title | Do it after | Why then |
|---|---|---|---|
| `challenge01` | Group Anagrams | Week 04 -- Data Structures | needs dicts, lists, and hashing, nothing more |
| `challenge02` | LRU Cache | Week 06 -- OOP I | needs classes, `__init__`, encapsulation |
| `challenge03` | Sales Data Analyzer | Week 10 -- Pandas | needs groupby/vectorized pandas, not raw loops |
| `challenge04` | Rate Limiter (Token Bucket) | Week 12 -- Requests + Threading | needs `threading.Lock` and real concurrency safety |
| `challenge05` | URL Shortener API | Week 13 -- FastAPI | needs routes, Pydantic models, and in-memory state |

The web reference (`presentation/index.html`) surfaces each challenge as a
callout on its assigned topic's page, with a link back to this folder.

## Why the constraints matter

Every challenge's `README.md` doesn't just describe *what* to build -- it
also mandates *how* to build it (a required technique, a forbidden
shortcut, or a specific interface), and asks for a comprehensive, written-out
list of the edge cases your solution handles. That's deliberate: a real
interview is judged on the same two things pytest can't check --
implementation choices and edge-case awareness -- not just on whether the
happy path returns the right answer.
