"""
Command-line interface for the Python Training test suite.

Usage (run from the repo root):
    python tools/cli.py list
    python tools/cli.py test week01
    python tools/cli.py test week01_exercise03
    python tools/cli.py test challenge01
    python tools/cli.py test --all
"""
import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import run_week_tests, run_all_tests, WEEKS, WEEK_TOPICS, CHALLENGES, EXERCISES


EXAMPLES = """\
examples:
  python tools/cli.py list                    list all 14 weeks, their exercises, and the challenges
  python tools/cli.py test week01              run every exercise in week01
  python tools/cli.py test week01_exercise03   run just that one exercise
  python tools/cli.py test challenge01         run one interview challenge's tests
  python tools/cli.py test --all               run the full test suite (weeks + challenges)
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

    subparsers.add_parser("list", help="List all available weeks, their exercises, and the interview challenges")

    test_parser = subparsers.add_parser(
        "test",
        help="Run tests for one week, one exercise, one challenge, or everything",
        description="Run tests for one week, one exercise within a week, one interview challenge, or everything.",
        epilog=(
            "examples:\n"
            "  python tools/cli.py test week01               run every exercise in week01\n"
            "  python tools/cli.py test week01_exercise03    run just that one exercise\n"
            "  python tools/cli.py test challenge01           run only challenge01's tests\n"
            "  python tools/cli.py test --all                 run every week's + challenge's tests\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    test_parser.add_argument(
        "week",
        nargs="?",
        help="e.g. week01, week01_exercise03, or challenge01 (see 'python tools/cli.py list')",
    )
    test_parser.add_argument("--all", action="store_true", help="Run every week's and challenge's tests")

    args = parser.parse_args()

    if args.command == "list":
        exercises_by_week = {}
        for ex_id in EXERCISES:
            week = ex_id.split("_exercise")[0]
            exercises_by_week.setdefault(week, []).append(ex_id)
        for w in WEEKS:
            week_exercises = exercises_by_week.get(w, [])
            print(f"{w}  -  {WEEK_TOPICS[w]}  ({len(week_exercises)} exercise{'s' if len(week_exercises) != 1 else ''})")
            for ex_id in week_exercises:
                print(f"    {ex_id}")
        print()
        print("Run a single exercise with, e.g., python tools/cli.py test week01_exercise03")
        print("Run a whole week (every exercise above) with, e.g., python tools/cli.py test week01")
        print()
        print("Interview challenges (see challenges/README.md):")
        for c in CHALLENGES:
            print(f"{c}")
        return

    if args.command == "test":
        valid_targets = WEEKS + EXERCISES + CHALLENGES
        if args.all:
            result = run_all_tests()
        elif args.week:
            if args.week not in valid_targets:
                print(
                    f"Unknown target: {args.week!r}. Expected one of week01-week14, "
                    f"a specific exercise like week01_exercise03, or "
                    f"challenge01-challenge10 (run 'python tools/cli.py list' to see them all).\n"
                    f"Example: python tools/cli.py test week01"
                )
                sys.exit(1)
            result = run_week_tests(args.week)
        else:
            print(
                "Specify a week/exercise/challenge or pass --all.\n"
                "Examples:\n"
                "  python tools/cli.py test week01\n"
                "  python tools/cli.py test week01_exercise03\n"
                "  python tools/cli.py test challenge01\n"
                "  python tools/cli.py test --all"
            )
            sys.exit(1)

        print(_colorize_pytest_output(result.stdout))
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)


if __name__ == "__main__":
    main()
