words = ["Python", "is", "awesome"]
longest_word = max(words, key=len)  # Używamy funkcji 'len' jako klucza
print(longest_word)  # Wypisze "awesome", ponieważ to słowo ma najwięcej liter

people = [
    {"name": "John", "age": 45},
    {"name": "Diana", "age": 35},
    {"name": "Zack", "age": 30}
]
oldest_person = max(people, key=lambda person: person["age"])
print(oldest_person)  # Wypisze słownik reprezentujący Johna, ponieważ ma on największy wiek
