from contextlib import contextmanager
from time import time, sleep


# to co przed yield to metoda __enter__
# yield to kod pod słówkiem with
# to co po yield to metoda __exit__

@contextmanager
def time_it():
    start = time()
    try:
        yield
    finally:
        stop = time()
        print(f"Duration: {stop - start}")


with time_it():
    sleep(1)


@contextmanager
def own_open(filename, mode="r"):
    file_handler = open(filename, mode)
    try:
        yield file_handler
    finally:
        file_handler.close()


with own_open("text.txt") as file, open("text2.txt", "w") as file2:
    file2.write(file.read())
