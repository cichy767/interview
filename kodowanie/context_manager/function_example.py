"""Context manager jako generator; sprzątanie zawsze w finally."""

from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory
from time import perf_counter, sleep


@contextmanager
def time_it():
    start = perf_counter()
    try:
        yield
    finally:
        print(f"Duration: {perf_counter() - start}")


@contextmanager
def own_open(filename, mode="r", **kwargs):
    file_handler = open(filename, mode, **kwargs)
    try:
        yield file_handler
    finally:
        file_handler.close()


if __name__ == "__main__":
    with time_it():
        sleep(1)

    # Samowystarczalny przykład, niezależny od bieżącego katalogu.
    with TemporaryDirectory() as directory:
        source = Path(directory) / "text.txt"
        target = Path(directory) / "text2.txt"
        source.write_text("Przykładowa treść", encoding="utf-8")
        with own_open(source, encoding="utf-8") as file:
            with own_open(target, "w", encoding="utf-8") as file2:
                file2.write(file.read())
        print(target.read_text(encoding="utf-8"))
