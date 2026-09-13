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


def main():
    parser = argparse.ArgumentParser(description="Python Training test runner")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="List all available weeks and their topics")

    test_parser = subparsers.add_parser("test", help="Run tests for one week or all weeks")
    test_parser.add_argument("week", nargs="?", help="e.g. week01")
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
                print(f"Unknown week: {args.week}. Run 'python tools/cli.py list' to see valid weeks.")
                sys.exit(1)
            result = run_week_tests(args.week)
        else:
            print("Specify a week (e.g. week01) or pass --all.")
            sys.exit(1)

        print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)


if __name__ == "__main__":
    main()
