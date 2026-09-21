# Interview Challenges

Twenty-six standalone, interview-style coding problems -- two for every
week that has its own topic list (Weeks 1-13; Week 14 is the capstone
and has no fixed topic list of its own to draw from) -- separate from the
graded weekly exercises in `exercises/`. They exist for a different
purpose:

- **Weekly exercises** (`exercises/weekNN/exerciseXX/`) are small,
  focused, and each one drills a single technique in isolation --
  graded automatically by `tests/test_weekNN_exerciseXX.py` via
  `python tools/cli.py test weekNN_exerciseXX` (or the whole week at
  once with `python tools/cli.py test weekNN`).
- **Challenges** (`challenges/challengeNN/`) are the opposite shape on
  purpose: each one is a single, realistic problem built to pull in *as
  many* of that week's keywords, dunders, modules, methods, and concepts
  as it can, the way an actual interview problem forces you to combine
  everything you know instead of exercising one idea at a time. More
  code, fewer hints, and a real specification instead of a single
  function signature. **Correctness** is graded the same way as a weekly
  exercise -- `tests/test_challengeNN.py` via `python tools/cli.py test
  challengeNN` -- but a green checkmark there only proves the happy path
  and the documented edge cases work. Each challenge's `README.md` also
  mandates specific implementation choices (a required technique, a
  forbidden shortcut, a specific interface) that pytest has no way to
  check; grade those by reading the code.

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

| Challenge | Title | LeetCode | Do it after |
|---|---|---|---|
| `challenge01` | Typed Config Loader | -- | Week 01 -- Python Fundamentals |
| `challenge02` | Identity, Equality, and a Login Prompt | -- | Week 01 -- Python Fundamentals |
| `challenge03` | Log Stream Parser and Scanner | -- | Week 02 -- Control Flow |
| `challenge04` | Batch Retry Simulator | -- | Week 02 -- Control Flow |
| `challenge05` | Pluggable Event Pipeline | -- | Week 03 -- Functions |
| `challenge06` | Streaming Metrics Aggregator | -- | Week 03 -- Functions |
| `challenge07` | Anagram Groups with Records | #49 | Week 04 -- Data Structures |
| `challenge08` | Longest Consecutive Run of Records | #128 | Week 04 -- Data Structures |
| `challenge09` | Log File Parser with a Custom Exception Chain | -- | Week 05 -- Files, Exceptions, Regex |
| `challenge10` | Log Text Utilities with a Custom Context Manager | -- | Week 05 -- Files, Exceptions, Regex |
| `challenge11` | LRU Cache with a Descriptor and Class-Level Stats | #146 | Week 06 -- OOP I |
| `challenge12` | Min Stack with Class-Level Push Stats | #155 | Week 06 -- OOP I |
| `challenge13` | Notification System with Mixins and ABCs | -- | Week 07 -- OOP II |
| `challenge14` | Shape Library with Protocols and Composition | -- | Week 07 -- OOP II |
| `challenge15` | Matrix: A Rich Numeric Type | -- | Week 08 -- The Python Data Model |
| `challenge16` | Transaction Ledger: Callable and Context Manager | -- | Week 08 -- The Python Data Model |
| `challenge17` | Directory Report Builder | -- | Week 09 -- OS, JSON, Datetime, XML |
| `challenge18` | XML Feed to Timezone-Aware Digest | -- | Week 09 -- OS, JSON, Datetime, XML |
| `challenge19` | Sales Data Analyzer | -- | Week 10 -- Pandas |
| `challenge20` | Two Sum, Pandas-Style, with Joins and Diagnostics | #1 | Week 10 -- Pandas |
| `challenge21` | Document Scanner Preprocessing Pipeline | -- | Week 11 -- OpenCV |
| `challenge22` | Face-Region Redactor | -- | Week 11 -- OpenCV |
| `challenge23` | Rate-Limited HTTP Client | -- | Week 12 -- Requests + Threading |
| `challenge24` | Bounded Job Queue with Retry and ThreadPoolExecutor | -- | Week 12 -- Requests + Threading |
| `challenge25` | URL Shortener API with Dependency-Injected Auth | -- | Week 13 -- FastAPI |
| `challenge26` | Underground System API with Live Diagnostics | #1396 | Week 13 -- FastAPI |

The web reference (`presentation/index.html`) surfaces both of a week's
challenges as callouts on its assigned topic's page, each with a link
back to this folder.

## Why these are integration problems, not single-topic drills

Split any one week's two challenges apart and you'll find most of that
week's keyword/dunder/module/method/concept list touched somewhere across
the pair -- not just the one headline technique a narrower version of the
same problem would need. `challenge15` (Matrix), for example, implements
ten of Week 8's fourteen dunders on one class; `challenge13`
(Notification System) combines an `abc.ABC` base, mixins, cooperative
`super()`, and `isinstance()`/duck typing dispatch in one problem. That's
deliberate: a trainee who's only ever exercised each idea in isolation
(as the weekly exercises intentionally do, one at a time) hasn't yet had
to decide how several of them fit together in the same piece of code --
which is exactly what a real interview, and real production code, asks
for. Expect these to take real, focused time, not a five-minute warm-up.

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
