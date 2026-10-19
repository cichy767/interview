"""Export Q2's assumptions in both plans, both answer keys and Polish guides.

Use 'all' to render base documents before guides so numbered companion links
point to the versions actually exported in this run.
"""

import argparse
import json
from pathlib import Path
import subprocess
import sys


def export_guides(*, include_general=True):
    import export_interview_pdfs as base
    from export_interviewer_handbook import main

    companions = {}
    manifest = base.ROOT / "tmp/pdfs/qa.json"
    if manifest.is_file():
        for entry in json.loads(manifest.read_text(encoding="utf-8")):
            for stem in base.TARGETS:
                filename = entry["file"]
                if filename == f"{stem}.pdf" or filename.startswith(f"{stem}_v"):
                    companions[stem] = base.OUT / filename

    main(
        "q2_platforma_aws_przewodnik_scenariusze_pl",
        title="Q2: platforma danych AWS - założenia i scenariusze odpowiedzi",
        subject="Karta założeń, przepływ danych, obciążenie, błędy, IAM, KMS i koszt",
        header="Q2: PLATFORMA DANYCH AWS",
        footer="Założenia scenariusza, wyjaśnienia i ocena odpowiedzi",
        expected_chapters=18,
        force_page_break_before=("2.", "18."),
        companion_paths=companions,
    )
    if include_general:
        main(companion_paths=companions)


def export_base():
    from export_reserve_question_pdfs import export_base as export_updated_documents

    export_updated_documents()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("group", choices=("all", "base", "guides"))
    args = parser.parse_args()
    if args.group == "all":
        for group in ("base", "guides"):
            subprocess.run([sys.executable, str(Path(__file__).resolve()), group], check=True)
    elif args.group == "base":
        export_base()
    else:
        export_guides()
