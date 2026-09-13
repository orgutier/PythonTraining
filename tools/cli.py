"""
Command-line interface for the Python Training test suite.

Usage (run from the repo root):
    python tools/cli.py list
    python tools/cli.py test week01
    python tools/cli.py test --all
"""
import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import run_week_tests, run_all_tests, WEEKS, WEEK_TOPICS


EXAMPLES = """\
examples:
  python tools/cli.py list              list all 14 weeks and their topics
  python tools/cli.py test week01       run the tests for week01 only
  python tools/cli.py test --all        run the full test suite
"""


def main():
    parser = argparse.ArgumentParser(
        description="Python Training test runner",
        epilog=EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="List all available weeks and their topics")

    test_parser = subparsers.add_parser(
        "test",
        help="Run tests for one week or all weeks",
        description="Run tests for one week or all weeks.",
        epilog=(
            "examples:\n"
            "  python tools/cli.py test week01       run only week01's tests\n"
            "  python tools/cli.py test --all        run every week's tests\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    test_parser.add_argument("week", nargs="?", help="e.g. week01 (see 'python tools/cli.py list')")
    test_parser.add_argument("--all", action="store_true", help="Run every week's tests")

    args = parser.parse_args()

    if args.command == "list":
        for w in WEEKS:
            print(f"{w}  -  {WEEK_TOPICS[w]}")
        return

    if args.command == "test":
        if args.all:
            result = run_all_tests()
        elif args.week:
            if args.week not in WEEKS:
                print(
                    f"Unknown week: {args.week!r}. Expected one of week01-week14 "
                    f"(run 'python tools/cli.py list' to see topics).\n"
                    f"Example: python tools/cli.py test week01"
                )
                sys.exit(1)
            result = run_week_tests(args.week)
        else:
            print(
                "Specify a week or pass --all.\n"
                "Examples:\n"
                "  python tools/cli.py test week01\n"
                "  python tools/cli.py test --all"
            )
            sys.exit(1)

        print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)


if __name__ == "__main__":
    main()
