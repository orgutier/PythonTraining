"""
Generates the full exercises/ , reference_solutions/ , and tests/ trees for
the PythonTraining repo. Run once from the repo root: `python generate.py`.

The actual exercise content lives in generator/stageNN.py, one module per
stage -- each defines STAGE, TOPIC, OVERVIEW, and EXERCISES (a list of
per-exercise dicts). This file just orchestrates them via
generator.common.write_stage(). Edit a stage's content in generator/stageNN.py,
not here, then re-run this script.

Running this regenerates exercises/*/solution.py back to their
NotImplementedError stubs -- handy after testing with a reference solution
swapped in (see the swap/test/regenerate workflow in each stage's own
verification, or just re-run this to reset).
"""
import importlib
import os

from generator.common import write_stage

ROOT = os.path.dirname(os.path.abspath(__file__))

STAGE_IDS = [f"stage{n:02d}" for n in range(1, 15)]


def main():
    generated = 0
    for stage_id in STAGE_IDS:
        try:
            mod = importlib.import_module(f"generator.{stage_id}")
        except ModuleNotFoundError:
            continue
        write_stage(ROOT, mod.STAGE, mod.TOPIC, mod.OVERVIEW, mod.EXERCISES)
        generated += 1
    print(f"Generated {generated} stages.")


if __name__ == "__main__":
    main()
