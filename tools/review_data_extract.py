"""
Step 1 of regenerating presentation-review/reviewdata.js.

Walks every generator/stageNN.py module (for exercise name/title/summary),
every exercises/stageNN/<name>/README.md, every reference_solutions/.../
solution.py, every challenges/challengeNN/README.md + its reference
solution, and every exams/examNN/README.md + its reference solution --
and dumps it all as JSON for review_data_build.js to consume.

Usage (from the repo root):
    python tools/review_data_extract.py <output_dir>

Writes <output_dir>/exercises.json and <output_dir>/challenges_exams.json.
"""
import sys
import json
import re
import importlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def extract_exercises():
    out = {}
    for n in range(1, 15):
        mod = importlib.import_module(f"generator.stage{n:02d}")
        stage_id = f"stage{n:02d}"
        items = []
        for ex in getattr(mod, "EXERCISES", []):
            name = ex["name"]
            ex_dir = ROOT / "exercises" / stage_id / name
            readme_path = ex_dir / "README.md"
            ref_sol_path = ROOT / "reference_solutions" / stage_id / name / "solution.py"
            items.append({
                "id": f"{stage_id}_{name}",
                "name": name,
                "title": ex.get("title", ""),
                "summary": ex.get("summary", ""),
                "readme": readme_path.read_text() if readme_path.exists() else "",
                "reference_solution": ref_sol_path.read_text() if ref_sol_path.exists() else "",
            })
        out[stage_id] = items
    return out


def extract_challenges_exams():
    challenges = {}
    for n in range(1, 27):
        cid = f"challenge{n:02d}"
        d = ROOT / "challenges" / cid
        readme = (d / "README.md").read_text() if (d / "README.md").exists() else ""
        sol_path = ROOT / "reference_solutions" / "challenges" / cid / "solution.py"
        m = re.search(r"Stage (\d+)", readme)
        stage = f"stage{int(m.group(1)):02d}" if m else None
        challenges[cid] = {
            "readme": readme,
            "solution": sol_path.read_text() if sol_path.exists() else "",
            "stage": stage,
        }

    exams = {}
    for n in range(1, 4):
        eid = f"exam{n:02d}"
        d = ROOT / "exams" / eid
        readme = (d / "README.md").read_text() if (d / "README.md").exists() else ""
        sol_path = ROOT / "reference_solutions" / "exams" / eid / "solution.py"
        m = re.search(r"Covers: Stages (\d+)-(\d+)", readme)
        lo, hi = (int(m.group(1)), int(m.group(2))) if m else (None, None)
        exams[eid] = {
            "readme": readme,
            "solution": sol_path.read_text() if sol_path.exists() else "",
            "lo": lo,
            "hi": hi,
        }

    return {"challenges": challenges, "exams": exams}


def main():
    if len(sys.argv) != 2:
        print("Usage: python tools/review_data_extract.py <output_dir>", file=sys.stderr)
        sys.exit(1)
    out_dir = Path(sys.argv[1])
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "exercises.json").write_text(json.dumps(extract_exercises(), indent=1))
    (out_dir / "challenges_exams.json").write_text(json.dumps(extract_challenges_exams(), indent=1))
    print(f"Wrote exercises.json and challenges_exams.json to {out_dir}")


if __name__ == "__main__":
    main()
