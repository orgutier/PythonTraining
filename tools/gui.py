"""
Simple GUI test runner. Lets trainees run their own exercise tests with a
button click, before they've learned any pytest or command-line syntax
(pytest itself isn't taught until Stage 11).

Pick a stage from the first dropdown, then either leave the second
dropdown on "All exercises (whole stage)" to test everything in that
stage, or pick one specific exercise (e.g. "tier1_basic01") to test just
that one -- the same two granularities `python tools/cli.py test` offers
(`test stage01` vs. `test stage01_tier1_basic01`). Only stages with at
least one exercise that actually has a tests/test_stageNN_*.py file show
up at all -- exercises are published weekly, stage by stage, so a stage
nobody's graded yet simply isn't in the dropdown instead of being pickable
and failing.

The git row shows the branch you're currently on, with three actions:
  - "Switch Branch..." checks out a different local branch, after a
    confirmation dialog (this can fail or interact badly with uncommitted
    changes, same as `git checkout` on the command line).
  - "Fetch" runs `git fetch origin`.
  - "Update" brings your branch up to date with origin/main and pushes the
    result back: stash any local changes, rebase onto origin/main, reapply
    the stash, then `git push --force-with-lease` your branch. It fetches
    first too, unless the last fetch (from either button) was under a
    minute ago. If the rebase hits a conflict, it's aborted and your stash
    is restored so the repo ends up exactly as it started, with a message
    telling you to resolve it manually. Refuses to run at all on
    main/master, since force-pushing there would rewrite shared history.

Run from the repo root:
    python tools/gui.py

Requires Tkinter, which ships with most standard Python installs. On some
Linux distros it needs a separate package, e.g.:
    sudo apt install python3-tk
"""
import os
import subprocess
import sys
import threading
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import run_stage_tests, run_all_tests, STAGES, STAGE_TOPICS, EXERCISES, REPO_ROOT

try:
    import tkinter as tk
    from tkinter import ttk, scrolledtext, messagebox
except ImportError:
    print("Tkinter is not installed. On Linux, try: sudo apt install python3-tk")
    sys.exit(1)


ALL_EXERCISES_LABEL = "All exercises (whole stage)"
NO_STAGES_LABEL = "(no exercises published yet)"

# A stage only shows up once at least one of its exercises has a real
# tests/test_stageNN_*.py file on disk (see core._discover_exercises) --
# never the full hardcoded STAGES range, so a stage that hasn't been
# published yet this week can't be picked and then fail to find anything
# to run.
PUBLISHED_STAGES = [s for s in STAGES if any(eid.startswith(s + "_") for eid in EXERCISES)]

GIT_FETCH_STALE_SECONDS = 60


def _git(args):
    """Run a git command in the repo root. Returns (returncode, stdout, stderr);
    never raises -- a missing git binary or similar comes back as a non-zero
    returncode with the exception text in stderr, same shape as a real git
    failure, so callers only need to check returncode."""
    try:
        result = subprocess.run(
            ["git"] + args, cwd=REPO_ROOT, capture_output=True, text=True,
        )
        return result.returncode, result.stdout, result.stderr
    except OSError as e:
        return 1, "", str(e)


def _exercises_for_stage(stage: str) -> list:
    """Every exercise id's suffix (e.g. "tier1_basic01") for one stage,
    derived from core.EXERCISES (itself derived from the filesystem) --
    never hardcoded, so it can't drift out of sync with generate.py."""
    prefix = stage + "_"
    return [eid[len(prefix):] for eid in EXERCISES if eid.startswith(prefix)]


class TestRunnerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Training - Test Runner")
        self.geometry("820x560")
        self.minsize(640, 420)

        self._last_fetch_time = None

        top = ttk.Frame(self, padding=10)
        top.pack(fill="x")

        ttk.Label(top, text="Stage:").pack(side="left")

        self.stage_labels = [f"{w} - {STAGE_TOPICS[w]}" for w in PUBLISHED_STAGES] or [NO_STAGES_LABEL]
        self.stage_var = tk.StringVar(value=self.stage_labels[0])
        self.stage_dropdown = ttk.Combobox(
            top, textvariable=self.stage_var, values=self.stage_labels,
            state="readonly" if PUBLISHED_STAGES else "disabled", width=45,
        )
        self.stage_dropdown.pack(side="left", padx=5)
        self.stage_dropdown.bind("<<ComboboxSelected>>", self._on_stage_changed)

        ttk.Label(top, text="Exercise:").pack(side="left", padx=(10, 0))

        self.exercise_var = tk.StringVar()
        self.exercise_dropdown = ttk.Combobox(
            top, textvariable=self.exercise_var,
            state="readonly" if PUBLISHED_STAGES else "disabled", width=22,
        )
        self.exercise_dropdown.pack(side="left", padx=5)
        if PUBLISHED_STAGES:
            self._on_stage_changed()

        self.run_button = ttk.Button(top, text="Run Tests", command=self.on_run)
        self.run_button.pack(side="left", padx=5)
        if not PUBLISHED_STAGES:
            self.run_button.config(state="disabled")

        self.run_all_button = ttk.Button(top, text="Run All Stages", command=self.on_run_all)
        self.run_all_button.pack(side="left", padx=5)

        git_row = ttk.Frame(self, padding=(10, 0, 10, 10))
        git_row.pack(fill="x")

        ttk.Label(git_row, text="Branch:").pack(side="left")
        self.branch_var = tk.StringVar(value=self._get_current_branch())
        ttk.Label(git_row, textvariable=self.branch_var, font=("Consolas", 10, "bold")).pack(side="left", padx=(5, 15))

        self.switch_button = ttk.Button(git_row, text="Switch Branch...", command=self.on_switch_branch)
        self.switch_button.pack(side="left", padx=5)

        self.fetch_button = ttk.Button(git_row, text="Fetch", command=self.on_fetch)
        self.fetch_button.pack(side="left", padx=5)

        self.update_button = ttk.Button(git_row, text="Update", command=self.on_update)
        self.update_button.pack(side="left", padx=5)

        self.status_var = tk.StringVar(value="Ready.")
        ttk.Label(self, textvariable=self.status_var, padding=(10, 0)).pack(fill="x")

        self.output = scrolledtext.ScrolledText(self, wrap="word", font=("Consolas", 10))
        self.output.pack(fill="both", expand=True, padx=10, pady=10)
        self.output.tag_config("pass", foreground="#1a7f37")
        self.output.tag_config("fail", foreground="#cf222e")
        self.output.tag_config("dim", foreground="#57606a")

    # ------------------------------------------------------------------
    # Stage/exercise selection
    # ------------------------------------------------------------------

    def _current_stage(self) -> str:
        return self.stage_var.get().split(" - ")[0]

    def _current_test_id(self) -> str:
        """The stage id alone (whole stage) if "All exercises" is picked,
        else "stageNN_<exercise>" for just that one exercise -- both
        shapes run_stage_tests() already understands."""
        stage = self._current_stage()
        exercise = self.exercise_var.get()
        if not exercise or exercise == ALL_EXERCISES_LABEL:
            return stage
        return f"{stage}_{exercise}"

    def _on_stage_changed(self, event=None):
        stage = self._current_stage()
        values = [ALL_EXERCISES_LABEL] + _exercises_for_stage(stage)
        self.exercise_dropdown.config(values=values)
        self.exercise_var.set(ALL_EXERCISES_LABEL)

    # ------------------------------------------------------------------
    # Output pane / shared button state / async helper
    # ------------------------------------------------------------------

    def _write(self, text: str):
        self.output.delete("1.0", tk.END)
        for line in text.splitlines():
            tag = None
            if "PASSED" in line:
                tag = "pass"
            elif "FAILED" in line or "ERROR" in line:
                tag = "fail"
            elif line.startswith("=") or line.startswith("-"):
                tag = "dim"
            self.output.insert(tk.END, line + "\n", tag)

    def _set_buttons_enabled(self, enabled: bool):
        state = "normal" if enabled else "disabled"
        test_state = state if PUBLISHED_STAGES else "disabled"
        self.run_button.config(state=test_state)
        self.run_all_button.config(state=state)
        self.switch_button.config(state=state)
        self.fetch_button.config(state=state)
        self.update_button.config(state=state)

    def _run_async(self, worker, on_done):
        """Run `worker()` (no args -- wrap with a lambda for args) on a
        background thread so the GUI never blocks, then marshal its result
        back onto the main thread for `on_done(result)` to render."""
        self._set_buttons_enabled(False)

        def task():
            result = worker()
            self.after(0, lambda: on_done(result))

        threading.Thread(target=task, daemon=True).start()

    # ------------------------------------------------------------------
    # Running tests
    # ------------------------------------------------------------------

    def _finish_tests(self, result):
        self._write(result.stdout + "\n" + result.stderr)
        passed = result.returncode == 0
        self.status_var.set("All tests passed." if passed else "Some tests failed - see above.")
        self._set_buttons_enabled(True)

    def on_run(self):
        test_id = self._current_test_id()
        self.status_var.set(f"Running {test_id}...")
        self._write(f"Running tests for {test_id}...\n")
        self._run_async(lambda: run_stage_tests(test_id), self._finish_tests)

    def on_run_all(self):
        self.status_var.set("Running all stages...")
        self._write("Running all stages...\n")
        self._run_async(run_all_tests, self._finish_tests)

    # ------------------------------------------------------------------
    # Git: branch display + switch
    # ------------------------------------------------------------------

    def _get_current_branch(self) -> str:
        code, out, err = _git(["rev-parse", "--abbrev-ref", "HEAD"])
        return out.strip() if code == 0 and out.strip() else "(unknown)"

    def _list_local_branches(self) -> list:
        code, out, err = _git(["branch", "--format=%(refname:short)"])
        if code != 0:
            return []
        return [b.strip() for b in out.splitlines() if b.strip()]

    def _prompt_branch_choice(self, branches: list):
        """Small modal dialog to pick one branch from a dropdown. Returns
        the chosen branch name, or None if cancelled."""
        dialog = tk.Toplevel(self)
        dialog.title("Choose a branch")
        dialog.transient(self)
        dialog.resizable(False, False)
        dialog.grab_set()

        ttk.Label(dialog, text="Switch to:").pack(padx=12, pady=(12, 4), anchor="w")
        choice_var = tk.StringVar(value=branches[0])
        combo = ttk.Combobox(dialog, textvariable=choice_var, values=branches, state="readonly", width=40)
        combo.pack(padx=12, pady=(0, 12))

        result = {"value": None}

        def on_ok():
            result["value"] = choice_var.get()
            dialog.destroy()

        def on_cancel():
            dialog.destroy()

        btns = ttk.Frame(dialog)
        btns.pack(pady=(0, 12))
        ttk.Button(btns, text="OK", command=on_ok).pack(side="left", padx=5)
        ttk.Button(btns, text="Cancel", command=on_cancel).pack(side="left", padx=5)

        dialog.protocol("WM_DELETE_WINDOW", on_cancel)
        dialog.wait_window()
        return result["value"]

    def on_switch_branch(self):
        current = self.branch_var.get()
        others = [b for b in self._list_local_branches() if b != current]
        if not others:
            messagebox.showinfo("Switch Branch", "No other local branches to switch to.")
            return

        target = self._prompt_branch_choice(others)
        if not target:
            return

        if not messagebox.askyesno(
            "Switch Branch",
            f"Switch from '{current}' to '{target}'?\n\n"
            "Make sure anything you want to keep is already committed or "
            "stashed -- switching can fail, or leave uncommitted changes "
            "carried over, if they conflict with the other branch.",
        ):
            return

        self.status_var.set(f"Switching to {target}...")
        self._write(f"Switching to branch '{target}'...\n")
        self._run_async(lambda: self._do_switch_branch(target), self._finish_switch_branch)

    def _do_switch_branch(self, target: str) -> dict:
        code, out, err = _git(["checkout", target])
        return {"ok": code == 0, "output": out + err, "branch": target}

    def _finish_switch_branch(self, result: dict):
        self._write(result["output"] or "(no output)")
        if result["ok"]:
            self.branch_var.set(result["branch"])
            self.status_var.set(f"Switched to {result['branch']}.")
            if PUBLISHED_STAGES:
                self._on_stage_changed()
        else:
            self.status_var.set("Branch switch failed - see output above.")
        self._set_buttons_enabled(True)

    # ------------------------------------------------------------------
    # Git: fetch
    # ------------------------------------------------------------------

    def on_fetch(self):
        self.status_var.set("Fetching from origin...")
        self._write("Fetching from origin...\n")
        self._run_async(self._do_fetch, self._finish_fetch)

    def _do_fetch(self) -> dict:
        code, out, err = _git(["fetch", "origin"])
        return {"ok": code == 0, "output": out + err}

    def _finish_fetch(self, result: dict):
        self._write(result["output"] or "(already up to date)")
        if result["ok"]:
            self._last_fetch_time = time.monotonic()
            self.status_var.set("Fetch complete.")
        else:
            self.status_var.set("Fetch failed - see output above.")
        self._set_buttons_enabled(True)

    # ------------------------------------------------------------------
    # Git: update (stash -> rebase origin/main -> stash pop -> push)
    # ------------------------------------------------------------------

    def on_update(self):
        current = self.branch_var.get()
        if current in ("main", "master"):
            messagebox.showerror(
                "Update",
                f"Refusing to run Update on '{current}'. Update rebases onto "
                "origin/main and force-pushes the result, which would rewrite "
                "shared history on the default branch. Switch to your own "
                "training/<username> branch first.",
            )
            return

        self.status_var.set(f"Updating {current}...")
        self._write(f"Updating branch '{current}'...\n")
        self._run_async(lambda: self._do_update(current), self._finish_update)

    def _do_update(self, branch: str) -> dict:
        lines = []

        # 1. Fetch first, unless the last fetch (from either button) was
        # under a minute ago.
        if self._last_fetch_time is None or (time.monotonic() - self._last_fetch_time) > GIT_FETCH_STALE_SECONDS:
            lines.append("Fetching from origin (last fetch was more than 1 minute ago)...")
            code, out, err = _git(["fetch", "origin"])
            lines.append(out + err)
            if code != 0:
                return {"ok": False, "output": "\n".join(lines), "status": "Update stopped: fetch failed - see output above."}
            self._last_fetch_time = time.monotonic()
        else:
            lines.append("Skipping fetch (last fetch was under a minute ago).")

        # 2. Stash local changes, if any.
        code, out, err = _git(["status", "--porcelain"])
        has_changes = bool(out.strip())
        stashed = False
        if has_changes:
            lines.append("Stashing local changes...")
            code, out, err = _git(["stash", "push", "-u", "-m", "gui-update-autostash"])
            lines.append(out + err)
            if code != 0:
                return {"ok": False, "output": "\n".join(lines), "status": "Update stopped: stashing your changes failed. Nothing else was touched."}
            stashed = True
        else:
            lines.append("No local changes to stash.")

        # 3. Rebase onto origin/main.
        lines.append("Rebasing onto origin/main...")
        code, out, err = _git(["rebase", "origin/main"])
        lines.append(out + err)
        if code != 0:
            # Leave the repo exactly as it started: abort the rebase, then
            # restore whatever we stashed.
            lines.append("Rebase hit a conflict -- aborting and restoring your changes...")
            _git(["rebase", "--abort"])
            if stashed:
                pop_code, pop_out, pop_err = _git(["stash", "pop"])
                lines.append(pop_out + pop_err)
                if pop_code != 0:
                    lines.append(
                        "WARNING: could not automatically restore your stashed changes "
                        "after aborting the rebase. They're still safe -- run "
                        "'git stash list' / 'git stash pop' yourself -- but this needs "
                        "manual attention."
                    )
            return {
                "ok": False,
                "output": "\n".join(lines),
                "status": (
                    "Update stopped: rebasing onto origin/main hit a conflict. The "
                    "rebase was aborted, so your repo is back the way it was. Resolve "
                    "this manually, or ask your instructor/support for help, then try "
                    "Update again."
                ),
            }

        # 4. Reapply the stash.
        if stashed:
            lines.append("Reapplying your stashed changes...")
            code, out, err = _git(["stash", "pop"])
            lines.append(out + err)
            if code != 0:
                return {
                    "ok": False,
                    "output": "\n".join(lines),
                    "status": (
                        "Update stopped: the rebase succeeded, but reapplying your "
                        "stashed changes hit a conflict. Your changes are still safe "
                        "in the stash -- resolve this manually, or ask your "
                        "instructor/support for help, then try again."
                    ),
                }

        # 5. Push the rebased branch back, force-with-lease (safe force --
        # refuses if the remote moved since our last fetch).
        lines.append(f"Pushing rebased '{branch}' to origin (force-with-lease)...")
        code, out, err = _git(["push", "--force-with-lease", "-u", "origin", f"{branch}:{branch}"])
        lines.append(out + err)
        if code != 0:
            return {
                "ok": False,
                "output": "\n".join(lines),
                "status": "Update stopped: rebase succeeded but the push failed - see output above.",
            }

        return {
            "ok": True,
            "output": "\n".join(lines),
            "status": f"'{branch}' is up to date with origin/main and pushed.",
        }

    def _finish_update(self, result: dict):
        self._write(result["output"])
        self.status_var.set(result["status"])
        if not result["ok"]:
            messagebox.showwarning("Update", result["status"])
        self._set_buttons_enabled(True)


if __name__ == "__main__":
    app = TestRunnerGUI()
    app.mainloop()
