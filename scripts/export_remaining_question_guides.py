"""Build the individual Polish Q3-Q6 guides and render their review previews."""

from export_interviewer_handbook import main


GUIDES = (
    dict(
        stem="q4_cicd_oidc_przewodnik_scenariusze_pl",
        title="Q4: CI/CD, OIDC i testy - przewodnik i scenariusze odpowiedzi",
        subject="Pipeline, tymczasowy dostęp do AWS, artefakty, testy danych i awarie wdrożeń",
        header="Q4: CI/CD, OIDC I TESTY",
        footer="Wyjaśnienia od podstaw, scenariusze i ocena odpowiedzi",
        expected_chapters=14,
        force_page_break_before=("14.",),
    ),
    dict(
        stem="q3_terraform_przewodnik_scenariusze_pl",
        title="Q3: Terraform w zespole - przewodnik i scenariusze odpowiedzi",
        subject="State, blokady, środowiska, częściowe błędy, drift i bezpieczeństwo danych",
        header="Q3: TERRAFORM W ZESPOLE",
        footer="Wyjaśnienia od podstaw, scenariusze i ocena odpowiedzi",
        expected_chapters=15,
        force_page_break_before=("15.",),
    ),
    dict(
        stem="q5_python_przewodnik_scenariusze_pl",
        title="Q5: Python - oba zadania, przewodnik i scenariusze odpowiedzi",
        subject="Wczesny return, współdzielona lista, warunki logiczne i automatyzacja",
        header="Q5: PYTHON I AUTOMATYZACJA",
        footer="Oba zadania krok po kroku, scenariusze i ocena odpowiedzi",
        expected_chapters=15,
        force_page_break_before=("15.",),
    ),
    dict(
        stem="q6_operacje_siec_przewodnik_scenariusze_pl",
        title="Q6: incydenty, sieć i komunikacja - przewodnik i scenariusze odpowiedzi",
        subject="Diagnostyka przepływu danych, idempotencja, replay, monitoring i VPC",
        header="Q6: INCYDENTY, SIEĆ I KOMUNIKACJA",
        footer="Wyjaśnienia od podstaw, scenariusze i ocena odpowiedzi",
        expected_chapters=16,
        force_page_break_before=("16.",),
    ),
)


if __name__ == "__main__":
    for guide in GUIDES:
        main(**guide)
