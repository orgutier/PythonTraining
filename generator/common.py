"""
Shared plumbing for the per-stage generator modules (generator/stageNN.py).

Each stage module defines STAGE, TOPIC, OVERVIEW, and EXERCISES (a list of
exercise dicts) -- write_stage() below turns that into the actual files:

    exercises/stageNN/README.md                  stage overview + exercise list
    exercises/stageNN/<name>/solution.py          stub, the entry point
    exercises/stageNN/<name>/README.md            that exercise's own description
    reference_solutions/stageNN/<name>/solution.py
    tests/test_stageNN_<name>.py                  that ONE exercise's tests

`<name>` is whatever each exercise dict's "name" field says -- historically
"exerciseXX" (still true for most stages), but a stage piloting the
tier-named convention (minimum two exercises per Basic/Mid/Advanced tier,
e.g. "basic01"/"basic02"/"mid01"/..., plus an optional "hello_world" for a
stage's Setup sub-stage) uses those names instead. write_stage() itself
doesn't care either way.

An exercise dict may also set "instructions" (a one-line override of the
stub's default "Implement the function(s)/class(es) below." -- see
SCRIPT_INSTRUCTIONS for the wording used by module-level, non-function-wrapped
exercises).

Every exercise lives in its own folder specifically so a trainee can add
helper submodules next to solution.py (e.g. exercises/stage04/exercise02/helpers.py)
without that ever colliding with another exercise's files. solution.py stays
the one filename tests import from in every exercise, in every stage.

Tests are one file per exercise, not one aggregated file per stage, so
"stageNN_<name>" is a first-class, independently-runnable test target
(`python tools/cli.py test stage01_basic01`) alongside the existing
stage-level target "stageNN" (`tools/core.py` runs every exercise test file
for that stage when asked for the plain stage id -- see run_stage_tests()).
This is what lets the git hooks test at two different granularities: a
pre-commit hook can test only the specific exercise(s) just staged, while
a pre-push hook can (if configured to) test the whole stage for any
exercise touched in it.
"""
import os

DEFAULT_INSTRUCTIONS = "Implement the function(s)/class(es) below."
SCRIPT_INSTRUCTIONS = (
    "Write plain top-level code below -- no function/class wrapper needed "
    "(or expected) for this one. Assign your answers to the exact variable "
    "names named in README.md; the tests import this module and read those "
    "variables directly."
)

STUB_HEADER = '''"""
{title}
{instructions}

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_{stage}_{exercise}.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/{stage}/{exercise}/ and import it as a submodule (e.g.
`from exercises.{stage}.{exercise} import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


'''


def write_stage(root, stage, topic, overview, exercises):
    ex_stage_dir = os.path.join(root, "exercises", stage)
    ref_stage_dir = os.path.join(root, "reference_solutions", stage)
    tests_dir = os.path.join(root, "tests")
    os.makedirs(ex_stage_dir, exist_ok=True)
    os.makedirs(ref_stage_dir, exist_ok=True)

    # Older generations of this stage wrote one aggregated tests/test_stageNN.py
    # instead of one file per exercise -- remove it so pytest doesn't also
    # pick up stale, duplicate copies of these same tests.
    stale_aggregate = os.path.join(tests_dir, f"test_{stage}.py")
    if os.path.exists(stale_aggregate):
        os.remove(stale_aggregate)

    listing = "\n".join(
        f"- **`{ex['name']}/`** -- {ex['summary']}" for ex in exercises
    )
    example_id = f"{stage}_{exercises[0]['name']}" if exercises else f"{stage}_<name>"
    with open(os.path.join(ex_stage_dir, "README.md"), "w") as f:
        f.write(
            f"# {topic}\n\n{overview}\n\n"
            f"## Exercises\n\n"
            f"Each exercise below lives in its own folder with its own "
            f"`solution.py` (the entry point) and `README.md` (the problem "
            f"statement), and is independently testable with "
            f"`python tools/cli.py test {stage}_<name>` (e.g. "
            f"`python tools/cli.py test {example_id}`). Work through "
            f"them in order.\n\n"
            f"{listing}\n"
        )

    for ex in exercises:
        name = ex["name"]
        ex_dir = os.path.join(ex_stage_dir, name)
        ref_dir = os.path.join(ref_stage_dir, name)
        os.makedirs(ex_dir, exist_ok=True)
        os.makedirs(ref_dir, exist_ok=True)

        with open(os.path.join(ex_dir, "solution.py"), "w") as f:
            f.write(
                STUB_HEADER.format(
                    title=f"{topic} -- {ex['title']}", stage=stage, exercise=name,
                    instructions=ex.get("instructions", DEFAULT_INSTRUCTIONS),
                )
                + ex["stub"]
            )
        with open(os.path.join(ex_dir, "README.md"), "w") as f:
            f.write(f"# {ex['title']}\n\n{ex['readme']}\n")
        with open(os.path.join(ref_dir, "solution.py"), "w") as f:
            f.write(ex["reference"])

        test_content = (
            f'"""\n'
            f"Tests for {stage}/{name} -- {topic}: {ex['title']}.\n"
            f"Auto-generated by generate.py from generator/{stage}.py -- edit "
            f"that file, not this one, then re-run `python generate.py`.\n"
            f'"""\n\n'
        ) + ex["test"]
        with open(os.path.join(tests_dir, f"test_{stage}_{name}.py"), "w") as f:
            f.write(test_content)
