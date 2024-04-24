"""
In Python, to safely retrieve a value from a dictionary without the risk of raising a KeyError
if the key does not exist, you can use several methods. Here are the most common approaches:
"""

my_dict = {'a': 1, 'b': 2}
value = my_dict.get('c', 'default')  # Returns 'default' since 'c' is not a key in the dictionary

my_dict_2 = {'a': 1, 'b': 2}
value_2 = my_dict_2.setdefault('c', 3)  # Since 'c' is not a key in the dictionary, it will be set to 3
print(value_2)  # Outputs: 3
print(my_dict_2)  # Outputs: {'a': 1, 'b': 2, 'c': 3}
