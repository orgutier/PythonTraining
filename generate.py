"""
Generates the full exercises/ , reference_solutions/ , and tests/ trees for
the PythonTraining repo. Run once from the repo root: `python generate.py`.

The actual exercise content lives in generator/weekNN.py, one module per
week -- each defines WEEK, TOPIC, OVERVIEW, and EXERCISES (a list of
per-exercise dicts). This file just orchestrates them via
generator.common.write_week(). Edit a week's content in generator/weekNN.py,
not here, then re-run this script.

Running this regenerates exercises/*/solution.py back to their
NotImplementedError stubs -- handy after testing with a reference solution
swapped in (see the swap/test/regenerate workflow in each week's own
verification, or just re-run this to reset).
"""
import importlib
import os

from generator.common import write_week

ROOT = os.path.dirname(os.path.abspath(__file__))

WEEK_IDS = [f"week{n:02d}" for n in range(1, 15)]


def main():
    generated = 0
    for week_id in WEEK_IDS:
        try:
            mod = importlib.import_module(f"generator.{week_id}")
        except ModuleNotFoundError:
            continue
        write_week(ROOT, mod.WEEK, mod.TOPIC, mod.OVERVIEW, mod.EXERCISES)
        generated += 1
    print(f"Generated {generated} weeks.")


if __name__ == "__main__":
    main()
