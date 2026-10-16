"""Leniwy odczyt rekordów; plik pozostaje otwarty podczas iteracji."""

from contextlib import closing
from itertools import islice
from pathlib import Path


def get_records(file_patch):
    # with zamknie plik przy wyczerpaniu generatora, close() lub wyjątku.
    with open(file_patch, encoding="utf-8") as file:
        for line in file:
            if ':' in line:
                msg_type, action = line.rstrip("\n").split(':', 1)
                yield msg_type, action


if __name__ == "__main__":
    source = Path(__file__).parent / "help" / "file.txt"
    # Przy wcześniejszym przerwaniu iteracji jawnie zamykamy generator.
    with closing(get_records(source)) as gen:
        for record in islice(gen, 2):
            print(record)
