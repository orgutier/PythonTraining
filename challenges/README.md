# Interview Challenges

Five standalone, interview-style coding problems, separate from the graded
weekly exercises in `exercises/`. They exist for a different purpose:

- **Weekly exercises** (`exercises/weekNN/`) are scoped tightly to that
  week's topic and are graded automatically by `tests/test_weekNN.py` via
  `python tools/cli.py test weekNN`.
- **Challenges** (`challenges/challengeNN/`) are the kind of problem an
  engineer is actually asked to write live in a technical interview: more
  code, fewer hints, and a real specification instead of a single function
  signature. **Correctness** is graded the same way as a weekly exercise
  -- `tests/test_challengeNN.py` via `python tools/cli.py test challengeNN`
  -- but a green checkmark there only proves the happy path and the
  documented edge cases work. Each challenge's `README.md` also mandates
  specific implementation choices (a required technique, a forbidden
  shortcut, a specific interface) that pytest has no way to check; grade
  those by reading the code.

Each `challengeNN/` folder has the same shape as a week's exercise:

```
challenges/challengeNN/
  README.md      Problem statement + specific constraints on HOW to write it
  solution.py     Stub with signatures/docstrings, raises NotImplementedError
```

with a matching pytest suite in `tests/test_challengeNN.py` and a worked
answer in `reference_solutions/challenges/challengeNN/` (both written and
verified against the same tests before being committed).

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
interview is judged on the same two things pytest can only partly check --
implementation choices and edge-case awareness -- not just on whether the
happy path returns the right answer. The pytest suite for each challenge
covers correctness and the documented edge cases; it does not (and can't,
in general) verify that you avoided the forbidden shortcut or used the
required technique -- that part is still a code-review job.
