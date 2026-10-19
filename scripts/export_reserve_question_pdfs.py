"""Export the R8 reserve guide and the five documents updated to include it.

Use 'all' to build all outputs and resolve links to numbered versions.
Candidate Python handouts and individual Q1-Q6 guides are not regenerated.
"""

import argparse
import json
from pathlib import Path
import subprocess
import sys


def export_guides():
    import export_interview_pdfs as base
    from export_interviewer_handbook import main

    manifest = base.ROOT / "tmp/pdfs/qa.json"
    companions = {}
    if manifest.is_file():
        for entry in json.loads(manifest.read_text(encoding="utf-8")):
            for stem in base.TARGETS:
                filename = entry["file"]
                if filename == f"{stem}.pdf" or filename.startswith(f"{stem}_v"):
                    companions[stem] = base.OUT / filename
    main(
        "r8_sekret_w_git_przewodnik_scenariusze_pl",
        title="R8: hasło w GitHub - rezerwowe pytanie i scenariusze odpowiedzi",
        subject="Pytanie na 2-4 minuty: sekret w Git, rotacja i sprawdzenie odbiorców",
        header="R8: HASŁO W GITHUB - PYTANIE REZERWOWE",
        footer="Wyjaśnienia, możliwe odpowiedzi i ściąga dla prowadzącego",
        expected_chapters=8,
        force_page_break_before=("8.",),
        companion_paths=companions,
    )
    main(companion_paths=companions)


def export_base():
    import export_interview_pdfs as base

    base.FILES = [item for item in base.FILES if item[0] != "zadanie_python_dla_kandydata"]
    # Handouts are read-only companions: retain their existing names in links.
    for stem in base.TARGETS:
        if stem.startswith("zadanie_python_dla_kandydata"):
            base.TARGETS[stem] = base.OUT / f"{stem}.pdf"
    base.main()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("group", choices=("all", "guides", "base"))
    args = parser.parse_args()
    if args.group == "all":
        # Bootstrap the new guide before base-link validation, then update
        # guide links after base export selects any necessary numbered paths.
        for group in ("guides", "base", "guides"):
            subprocess.run([sys.executable, str(Path(__file__).resolve()), group], check=True)
    elif args.group == "guides":
        export_guides()
    else:
        export_base()
