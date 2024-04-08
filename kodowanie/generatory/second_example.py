def square_numbers(nums):
    for i in nums:
        yield i * i


my_nums = square_numbers([1, 2, 3, 4, 5])

print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))

# generator można osiągnąć używając list comprehension, ale zamieniając nawiasy kwadratowe na okrągłe
my_nums = (x * x for x in [1, 2, 3, 4, 5])

print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
