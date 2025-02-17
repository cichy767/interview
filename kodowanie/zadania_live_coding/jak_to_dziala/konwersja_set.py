# Jak efetywnie przeszukać gigantyczną listę?
# Można zamienić listę na set. Konwersja na set zajmie trochę czasu, ale dzieki temu potem wyszukiwanie bedzie szybsze.

# 🛠️ Rekomendacja
# Jeśli sprawdzasz wartość tylko raz, użyj list (unikniesz kosztu konwersji).
# Jeśli masz dużą ilość wyszukiwań, konwertuj list do set tylko raz na początku – potem wyszukiwanie będzie superszybkie. 🚀


import time

values_list = list(range(10 ** 6))  # Lista 1 miliona elementów
values_set = set(values_list)  # Set 1 miliona elementów

search_element = 999999  # Element na końcu

# Wyszukiwanie w liście
start_time = time.time()
found = search_element in values_list
print(f"Lista: {time.time() - start_time:.6f} s")

# Wyszukiwanie w zbiorze
start_time = time.time()
found = search_element in values_set
print(f"Set: {time.time() - start_time:.6f} s")

# Wyszukiwanie w zbiorze z knowersja z listy na zbior
start_time = time.time()
converted_set = set(values_list)
found = search_element in converted_set
print(f"Converted: {time.time() - start_time:.6f} s")
