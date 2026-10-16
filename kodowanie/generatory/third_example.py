from kodowanie.generatory.help import mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


if __name__ == "__main__":
    # Uruchom z katalogu repo: python -m kodowanie.generatory.third_example
    print(f'Memory (Before): {mem_profile.memory_usage_psutil():.2f} MiB')
    start = time.perf_counter()
    people = people_generator(1000000)
    created = time.perf_counter()
    print(f'Generator creation: {created - start:.6f} seconds')
    # Utworzenie generatora nie wykonuje jego ciała; dopiero iteracja tworzy dane.
    count = sum(1 for _ in people)
    print(f'Generated {count} records in {time.perf_counter() - created:.3f} seconds')
    print(f'Memory (After): {mem_profile.memory_usage_psutil():.2f} MiB')
