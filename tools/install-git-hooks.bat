@echo off
rem Installs this repo's git hooks (pre-commit and pre-push) on Windows.
rem Run this once after cloning: tools\install-git-hooks.bat
rem
rem It points git at the tracked .githooks\ folder (git config
rem core.hooksPath), so pre-commit and pre-push both run the full test
rem suite -- every week's exercise tests AND every interview challenge's
rem tests -- via "python tools\cli.py test --all". See README.md,
rem section "Git hook integration".

setlocal

set "SCRIPT_DIR=%~dp0"
set "REPO_ROOT=%SCRIPT_DIR%.."

pushd "%REPO_ROOT%" 2>nul
if errorlevel 1 (
    echo Could not locate the repository root next to this script.
    exit /b 1
)

git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
    echo This does not look like a git repository: %CD%
    popd
    exit /b 1
)

if not exist ".githooks\pre-commit" (
    echo .githooks\pre-commit not found in %CD% -- nothing to install.
    popd
    exit /b 1
)
if not exist ".githooks\pre-push" (
    echo .githooks\pre-push not found in %CD% -- nothing to install.
    popd
    exit /b 1
)

git config core.hooksPath .githooks
if errorlevel 1 (
    echo Failed to set core.hooksPath.
    popd
    exit /b 1
)

echo.
echo Git hooks installed.
echo   core.hooksPath = .githooks
echo   pre-commit and pre-push will now run: python tools\cli.py test --all
echo.
echo Skip a single check when you really need to with:
echo   git commit --no-verify
echo   git push --no-verify
echo.

popd
endlocal
exit /b 0
