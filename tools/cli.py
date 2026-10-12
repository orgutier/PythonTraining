"""
Command-line interface for the Python Training test suite.

Usage (run from the repo root):
    python tools/cli.py list
    python tools/cli.py test stage01
    python tools/cli.py test stage01_exercise03
    python tools/cli.py test challenge01
    python tools/cli.py test --all
"""
import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import run_stage_tests, run_all_tests, STAGES, STAGE_TOPICS, CHALLENGES, EXERCISES, EXAMS


EXAMPLES = """\
examples:
  python tools/cli.py list                    list all 14 stages, their exercises, the challenges, and the exams
  python tools/cli.py test stage01              run every exercise in stage01
  python tools/cli.py test stage01_tier1_basic01  run just that one exercise (every stage but the
                                                 Capstone uses tier-named exercises -- tier0_hello_world/
                                                 tier1_basicNN/tier2_midNN/tier3_advancedNN/tier4_testing;
                                                 the Capstone stage still uses exercise01/02/...)
  python tools/cli.py test challenge01         run one interview challenge's tests
  python tools/cli.py test exam01              run one evaluation exam's tests
  python tools/cli.py test --all               run the full test suite (stages + challenges + exams)
"""

# Same PASSED/FAILED-ERROR/separator color scheme as the "pass"/"fail"/"dim"
# tags in tools/gui.py, so pytest output looks consistent across both tools.
_ANSI_GREEN = "\033[32m"
_ANSI_RED = "\033[31m"
_ANSI_DIM = "\033[2m"
_ANSI_RESET = "\033[0m"


def _colorize_pytest_output(text: str) -> str:
    if not sys.stdout.isatty():
        return text
    lines = []
    for line in text.splitlines():
        if "PASSED" in line:
            lines.append(f"{_ANSI_GREEN}{line}{_ANSI_RESET}")
        elif "FAILED" in line or "ERROR" in line:
            lines.append(f"{_ANSI_RED}{line}{_ANSI_RESET}")
        elif line.startswith("=") or line.startswith("-"):
            lines.append(f"{_ANSI_DIM}{line}{_ANSI_RESET}")
        else:
            lines.append(line)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Python Training test runner",
        epilog=EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="List all available stages, their exercises, the interview challenges, and the evaluation exams")

    test_parser = subparsers.add_parser(
        "test",
        help="Run tests for one stage, one exercise, one challenge, one exam, or everything",
        description="Run tests for one stage, one exercise within a stage, one interview challenge, one evaluation exam, or everything.",
        epilog=(
            "examples:\n"
            "  python tools/cli.py test stage01               run every exercise in stage01\n"
            "  python tools/cli.py test stage01_exercise03    run just that one exercise\n"
            "  python tools/cli.py test challenge01           run only challenge01's tests\n"
            "  python tools/cli.py test exam01                run only exam01's tests\n"
            "  python tools/cli.py test --all                 run every stage's + challenge's + exam's tests\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    test_parser.add_argument(
        "stage",
        nargs="?",
        help="e.g. stage01, stage01_exercise03, challenge01, or exam01 (see 'python tools/cli.py list')",
    )
    test_parser.add_argument("--all", action="store_true", help="Run every stage's, challenge's, and exam's tests")

    args = parser.parse_args()

    if args.command == "list":
        exercises_by_stage = {}
        for ex_id in EXERCISES:
            stage = ex_id.split("_", 1)[0]
            exercises_by_stage.setdefault(stage, []).append(ex_id)
        for w in STAGES:
            stage_exercises = exercises_by_stage.get(w, [])
            print(f"{w}  -  {STAGE_TOPICS[w]}  ({len(stage_exercises)} exercise{'s' if len(stage_exercises) != 1 else ''})")
            for ex_id in stage_exercises:
                print(f"    {ex_id}")
        print()
        print("Run a single exercise with, e.g., python tools/cli.py test stage01_exercise03")
        print("Run a whole stage (every exercise above) with, e.g., python tools/cli.py test stage01")
        print()
        print("Interview challenges (see challenges/README.md):")
        for c in CHALLENGES:
            print(f"{c}")
        print()
        print("Evaluation exams (see exams/README.md):")
        for e in EXAMS:
            print(f"{e}")
        return

    if args.command == "test":
        valid_targets = STAGES + EXERCISES + CHALLENGES + EXAMS
        if args.all:
            result = run_all_tests()
        elif args.stage:
            if args.stage not in valid_targets:
                print(
                    f"Unknown target: {args.stage!r}. Expected one of stage01-stage14, "
                    f"a specific exercise like stage01_exercise03, "
                    f"challenge01-challenge26, or exam01-exam03 "
                    f"(run 'python tools/cli.py list' to see them all).\n"
                    f"Example: python tools/cli.py test stage01"
                )
                sys.exit(1)
            result = run_stage_tests(args.stage)
        else:
            print(
                "Specify a stage/exercise/challenge/exam or pass --all.\n"
                "Examples:\n"
                "  python tools/cli.py test stage01\n"
                "  python tools/cli.py test stage01_exercise03\n"
                "  python tools/cli.py test challenge01\n"
                "  python tools/cli.py test exam01\n"
                "  python tools/cli.py test --all"
            )
            sys.exit(1)

        print(_colorize_pytest_output(result.stdout))
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)


if __name__ == "__main__":
    main()
