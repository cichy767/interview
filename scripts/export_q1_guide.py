"""Build only the Q1 S3 migration scenario guide and its review previews."""

from export_interviewer_handbook import main


if __name__ == "__main__":
    main(
        "q1_migracja_s3_przewodnik_scenariusze_pl",
        title="Q1: migracja S3 między kontami - przewodnik i scenariusze odpowiedzi",
        subject="Ocena własnego wkładu, replikacji S3 i alternatywnych scenariuszy migracji",
        header="Q1: MIGRACJA S3 MIĘDZY KONTAMI",
        footer="Pytania, scenariusze odpowiedzi i wskazówki do oceny",
        expected_chapters=15,
        force_page_break_before=("15.",),
    )
