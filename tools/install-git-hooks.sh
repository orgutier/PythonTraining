#!/bin/sh
# Installs this repo's git hooks (pre-commit and pre-push) on macOS/Linux.
# Run this once after cloning: sh tools/install-git-hooks.sh
#
# It points git at the tracked .githooks/ folder (git config
# core.hooksPath), so pre-commit and pre-push both run the full test
# suite -- every week's exercise tests AND every interview challenge's
# tests -- via "python tools/cli.py test --all". See README.md, section
# "Git hook integration". Windows trainees should run
# tools\install-git-hooks.bat instead.

set -e

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
REPO_ROOT="$SCRIPT_DIR/.."
cd "$REPO_ROOT"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "This does not look like a git repository: $(pwd)" >&2
    exit 1
fi

if [ ! -f ".githooks/pre-commit" ] || [ ! -f ".githooks/pre-push" ]; then
    echo ".githooks/pre-commit or .githooks/pre-push not found in $(pwd) -- nothing to install." >&2
    exit 1
fi

chmod +x .githooks/pre-commit .githooks/pre-push
git config core.hooksPath .githooks

echo ""
echo "Git hooks installed."
echo "  core.hooksPath = .githooks"
echo "  pre-commit and pre-push will now run: python tools/cli.py test --all"
echo ""
echo "Skip a single check when you really need to with:"
echo "  git commit --no-verify"
echo "  git push --no-verify"
echo ""
