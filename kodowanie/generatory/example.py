# lazy evaluation - generowanie wartości dopiero gdy są one potrzebne. funkcja wykonuje się z opóźnieniem. nie jest ładowane wszystko od razu do pamięci
# zamiast listy można przekazywać generator

def get_records(file_patch):
    print("----opening file----")
    file = open(file_patch)

    for line in file:
        if ':' in line:
            msg_type, action = line.rstrip("\n").split(':', 1)
            record = (msg_type, action)
            yield record

    print("----closing file----")
    file.close()


# for r in get_records('file.txt'):
#     print(f"The type is {r[0]} and the action is: {r[1]}.")

gen = get_records('help/file.txt')
r1 = next(gen)
print(r1)
r2 = next(gen)
