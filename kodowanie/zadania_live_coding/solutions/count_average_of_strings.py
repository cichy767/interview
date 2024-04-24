"""
Napisz funkcję która:
Usunie znaki specjalne ze zdań i policzy średnią znaków w słowach.
"""

string_1 = "W Szczebrzeszynie chrząszcz brzmi w trzcienie!"
string_2 = "Myślę, więc jestem... I znikam!"

import string


def average_word_length(sentence):
    # Usuwanie znaków specjalnych
    translator = str.maketrans('', '', string.punctuation)
    cleaned_sentence = sentence.translate(translator)

    # Podział zdania na słowa
    words = cleaned_sentence.split()

    # Obliczenie średniej długości słów, jeśli lista słów nie jest pusta
    if words:
        average_length = sum(len(word) for word in words) / len(words)
    else:
        average_length = 0

    return average_length


# Przykładowe wywołania funkcji
string_1 = "W Szczebrzeszynie chrząszcz brzmi w trzcienie!"
string_2 = "Myślę, więc jestem... I znikam!"

print(average_word_length(string_1))  # Przykład dla string_1
print(average_word_length(string_2))  # Przykład dla string_2