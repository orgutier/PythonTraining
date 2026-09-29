"""
Simple GUI test runner. Lets trainees run their own exercise tests with a
button click, before they've learned any pytest or command-line syntax
(pytest itself isn't taught until Stage 11).

Pick a stage from the first dropdown, then either leave the second
dropdown on "All exercises (whole stage)" to test everything in that
stage, or pick one specific exercise (e.g. "tier1_basic01") to test just
that one -- the same two granularities `python tools/cli.py test` offers
(`test stage01` vs. `test stage01_tier1_basic01`).

Run from the repo root:
    python tools/gui.py

Requires Tkinter, which ships with most standard Python installs. On some
Linux distros it needs a separate package, e.g.:
    sudo apt install python3-tk
"""
import os
import sys
import threading

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import run_stage_tests, run_all_tests, STAGES, STAGE_TOPICS, EXERCISES

try:
    import tkinter as tk
    from tkinter import ttk, scrolledtext
except ImportError:
    print("Tkinter is not installed. On Linux, try: sudo apt install python3-tk")
    sys.exit(1)


ALL_EXERCISES_LABEL = "All exercises (whole stage)"


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
        self.geometry("780x520")
        self.minsize(600, 400)

        top = ttk.Frame(self, padding=10)
        top.pack(fill="x")

        ttk.Label(top, text="Stage:").pack(side="left")

        self.stage_labels = [f"{w} - {STAGE_TOPICS[w]}" for w in STAGES]
        self.stage_var = tk.StringVar(value=self.stage_labels[0])
        self.stage_dropdown = ttk.Combobox(
            top, textvariable=self.stage_var, values=self.stage_labels,
            state="readonly", width=45,
        )
        self.stage_dropdown.pack(side="left", padx=5)
        self.stage_dropdown.bind("<<ComboboxSelected>>", self._on_stage_changed)

        ttk.Label(top, text="Exercise:").pack(side="left", padx=(10, 0))

        self.exercise_var = tk.StringVar()
        self.exercise_dropdown = ttk.Combobox(
            top, textvariable=self.exercise_var,
            state="readonly", width=22,
        )
        self.exercise_dropdown.pack(side="left", padx=5)
        self._on_stage_changed()

        self.run_button = ttk.Button(top, text="Run Tests", command=self.on_run)
        self.run_button.pack(side="left", padx=5)

        self.run_all_button = ttk.Button(top, text="Run All Stages", command=self.on_run_all)
        self.run_all_button.pack(side="left", padx=5)

        self.status_var = tk.StringVar(value="Ready.")
        ttk.Label(self, textvariable=self.status_var, padding=(10, 0)).pack(fill="x")

        self.output = scrolledtext.ScrolledText(self, wrap="word", font=("Consolas", 10))
        self.output.pack(fill="both", expand=True, padx=10, pady=10)
        self.output.tag_config("pass", foreground="#1a7f37")
        self.output.tag_config("fail", foreground="#cf222e")
        self.output.tag_config("dim", foreground="#57606a")

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
        self.run_button.config(state=state)
        self.run_all_button.config(state=state)

    def _run_in_thread(self, target, *args):
        self._set_buttons_enabled(False)

        def task():
            result = target(*args)
            self.after(0, lambda: self._finish(result))

        threading.Thread(target=task, daemon=True).start()

    def _finish(self, result):
        self._write(result.stdout + "\n" + result.stderr)
        passed = result.returncode == 0
        self.status_var.set("All tests passed." if passed else "Some tests failed - see above.")
        self._set_buttons_enabled(True)

    def on_run(self):
        test_id = self._current_test_id()
        self.status_var.set(f"Running {test_id}...")
        self._write(f"Running tests for {test_id}...\n")
        self._run_in_thread(run_stage_tests, test_id)

    def on_run_all(self):
        self.status_var.set("Running all stages...")
        self._write("Running all stages...\n")
        self._run_in_thread(run_all_tests)


if __name__ == "__main__":
    app = TestRunnerGUI()
    app.mainloop()
