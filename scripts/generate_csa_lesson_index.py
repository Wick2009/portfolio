#!/usr/bin/env python3
"""
Scans _notebooks/CSA/ap_mcq_lessons/unit_0[1-4] and builds _data/csa_units.yml.

This does NOT read or summarize lesson content. It only looks at structural
signals every notebook already carries -- front matter (title/permalink) and
cell count -- to flag which lesson numbers are fully-written vs. empty
placeholder stubs, and to group homework/backup files under their lesson
number. Re-run this any time notebooks are added, edited, or removed:

    python3 scripts/generate_csa_lesson_index.py
"""
import json
import re
import glob
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS_DIR = os.path.join(REPO_ROOT, "_notebooks", "CSA", "ap_mcq_lessons")
OUT_PATH = os.path.join(REPO_ROOT, "_data", "csa_units.yml")

NUMBER_RE = re.compile(r"(\d+)\.(\d+)")
QUIZ_RE = re.compile(r"u(\d+)quiz", re.IGNORECASE)


def parse_front_matter(cells):
    """Pull title/permalink out of the leading raw front-matter cell."""
    if not cells:
        return {}
    src = "".join(cells[0].get("source", []))
    fm = {}
    for line in src.splitlines():
        if ":" in line and not line.strip().startswith("---"):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if key and key not in fm:  # keep first occurrence (some files repeat keys)
                fm[key] = val
    return fm


def load_notebook(path):
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    cells = nb.get("cells", [])
    fm = parse_front_matter(cells)
    total_chars = sum(len("".join(c.get("source", []))) for c in cells)
    return {
        "cell_count": len(cells),
        "char_count": total_chars,
        "title": fm.get("title", ""),
        "permalink": fm.get("permalink", ""),
        "is_stub": len(cells) <= 1,
    }


def classify_file(filename):
    lower = filename.lower()
    if "backup" in lower:
        return "backup"
    if "homework" in lower or re.search(r"hw(?=\.ipynb$)", lower):
        return "homework"
    return "primary"


def main():
    units = []
    for unit_num in range(1, 5):
        unit_key = f"unit_{unit_num:02d}"
        unit_dir = os.path.join(LESSONS_DIR, unit_key)
        files = sorted(glob.glob(os.path.join(unit_dir, "*.ipynb")))

        lessons = {}  # lesson number string -> entry
        quiz_entry = None

        for path in files:
            filename = os.path.basename(path)
            data = load_notebook(path)
            rel_path = os.path.relpath(path, REPO_ROOT)

            quiz_match = QUIZ_RE.search(filename)
            if quiz_match:
                quiz_entry = {
                    "label": f"Unit {unit_num} Quiz",
                    "path": rel_path,
                    "permalink": data["permalink"],
                    "is_stub": data["is_stub"],
                }
                continue

            num_match = NUMBER_RE.search(filename)
            if not num_match:
                continue
            lesson_num = f"{num_match.group(1)}.{num_match.group(2)}"
            kind = classify_file(filename)

            entry = lessons.setdefault(lesson_num, {
                "number": lesson_num,
                "title": "",
                "permalink": "",
                "is_stub": True,
                "path": "",
                "extras": [],
            })

            if kind == "primary":
                # A real (non-stub) file always wins over a stub if both exist
                # under the same number for some reason.
                if not entry["path"] or (entry["is_stub"] and not data["is_stub"]):
                    entry["title"] = data["title"]
                    entry["permalink"] = data["permalink"]
                    entry["is_stub"] = data["is_stub"]
                    entry["path"] = rel_path
            else:
                entry["extras"].append({"kind": kind, "path": rel_path})

        def sort_key(n):
            major, minor = n.split(".")
            return (int(major), int(minor))

        lesson_list = [lessons[n] for n in sorted(lessons.keys(), key=sort_key)]
        real_count = sum(1 for l in lesson_list if not l["is_stub"])
        stub_count = len(lesson_list) - real_count
        first_real = next((l for l in lesson_list if not l["is_stub"]), None)

        units.append({
            "unit": unit_num,
            "lessons": lesson_list,
            "quiz": quiz_entry,
            "real_count": real_count,
            "stub_count": stub_count,
            "first_real_permalink": first_real["permalink"] if first_real else "",
        })

    write_yaml(units)
    total_real = sum(u["real_count"] for u in units)
    total_stub = sum(u["stub_count"] for u in units)
    print(f"Wrote {OUT_PATH}")
    print(f"Totals: {total_real} real lessons, {total_stub} empty stubs across units 1-4")


def yaml_str(s):
    s = s.replace('"', '\\"')
    return f'"{s}"'


def write_yaml(units):
    lines = []
    for u in units:
        lines.append(f"- unit: {u['unit']}")
        lines.append(f"  real_count: {u['real_count']}")
        lines.append(f"  stub_count: {u['stub_count']}")
        lines.append(f"  first_real_permalink: {yaml_str(u['first_real_permalink'])}")
        if u["quiz"]:
            q = u["quiz"]
            lines.append("  quiz:")
            lines.append(f"    label: {yaml_str(q['label'])}")
            lines.append(f"    path: {yaml_str(q['path'])}")
            lines.append(f"    permalink: {yaml_str(q['permalink'])}")
            lines.append(f"    is_stub: {str(q['is_stub']).lower()}")
        else:
            lines.append("  quiz: null")
        lines.append("  lessons:")
        for l in u["lessons"]:
            lines.append(f"    - number: {yaml_str(l['number'])}")
            lines.append(f"      title: {yaml_str(l['title'])}")
            lines.append(f"      permalink: {yaml_str(l['permalink'])}")
            lines.append(f"      is_stub: {str(l['is_stub']).lower()}")
            lines.append(f"      path: {yaml_str(l['path'])}")
            if l["extras"]:
                lines.append("      extras:")
                for e in l["extras"]:
                    lines.append(f"        - kind: {yaml_str(e['kind'])}")
                    lines.append(f"          path: {yaml_str(e['path'])}")
            else:
                lines.append("      extras: []")

    header = (
        "# AUTO-GENERATED by scripts/generate_csa_lesson_index.py\n"
        "# Do not hand-edit -- re-run the script instead.\n"
    )
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(header + "\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
