"""
Simple GUI test runner. Lets trainees run their own exercise tests with a
button click, before they've learned any pytest or command-line syntax
(pytest itself isn't taught until Stage 11).

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
from core import run_stage_tests, run_all_tests, STAGES, STAGE_TOPICS

try:
    import tkinter as tk
    from tkinter import ttk, scrolledtext
except ImportError:
    print("Tkinter is not installed. On Linux, try: sudo apt install python3-tk")
    sys.exit(1)


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
        stage = self._current_stage()
        self.status_var.set(f"Running {stage}...")
        self._write(f"Running tests for {stage}...\n")
        self._run_in_thread(run_stage_tests, stage)

    def on_run_all(self):
        self.status_var.set("Running all stages...")
        self._write("Running all stages...\n")
        self._run_in_thread(run_all_tests)


if __name__ == "__main__":
    app = TestRunnerGUI()
    app.mainloop()
