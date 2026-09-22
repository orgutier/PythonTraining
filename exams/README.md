# Evaluation Exams

Three checkpoint exams, each covering a run of stages -- not a single
stage, and not the whole course. They exist for a different purpose than
either the stage exercises or the interview challenges:

- **Stage exercises** (`exercises/stageNN/exerciseXX/`) drill one
  technique from one stage in isolation.
- **Interview challenges** (`challenges/challengeNN/`) integrate as much
  of *one* stage's material as possible into one realistic problem.
- **Exams** (`exams/examNN/`) integrate as much material as possible
  from *several consecutive stages* into one connected system -- proof
  you can still combine everything from that whole run of stages, not
  just the one you finished most recently.

| Exam | Title | Covers |
|---|---|---|
| `exam01` | Order Processing Pipeline | Stages 1-4 -- Python Fundamentals, Control Flow, Functions, Data Structures |
| `exam02` | Document Archive System | Stages 5-9 -- Files/Exceptions/Regex, OOP I, OOP II, the Data Model, OS/JSON/Datetime/XML |
| `exam03` | Product Analytics & Photo Pipeline API | Stages 10-13 -- Pandas, OpenCV, Requests + Threading, FastAPI |

Each `examNN/` folder has the same shape as a stage exercise or
challenge:

```
exams/examNN/
  README.md      Problem statement, one section per stage it covers
  solution.py     Stub with signatures/docstrings, raises NotImplementedError
```

with a matching pytest suite in `tests/test_examNN.py` and a worked
answer in `reference_solutions/exams/examNN/` (both written and verified
against the same tests before being committed). Run one with
`python tools/cli.py test examNN`, same as any exercise or challenge.

## Not required, but not optional either

Unlike the interview challenges (explicitly "not must-to"), an exam is a
checkpoint on the stages it covers -- it exists to catch material from
earlier stages that got exercised once and then forgotten, before you're
several more stages past it. `tools/report.py` tracks exams on their own
sheet, separate from both the required stage exercises and the optional
challenges, so a shareholder can see checkpoint results without them
being averaged into (or diluting) either of the other two.
