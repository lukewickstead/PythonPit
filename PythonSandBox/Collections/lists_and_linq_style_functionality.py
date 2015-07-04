# lists_and_linq_style_functionality.py
#
# Lists and Linq Style Functionality
#

import functools


def add(one, two):
    return one + two


def square(to_square):
    return to_square ** 2


def is_even(x):
    return x % 2 == 0


numbers = list(range(0, 10))

# Min/Max/Sum/In/Not In
print("Numbers:", numbers)
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))
print("1 in:", 1 in numbers)
print("10 not in", 10 not in numbers)
print("[1,2] in [[1,2],[1,1]]", [1, 2] in [[1, 2], [1, 1]])

# Filter where. Applies a predicate to an element.
print("\nFilter Is Even:")
for even_number in filter(is_even, range(0, 5)):
    print(even_number)

for even_number in filter(lambda x: x % 2 == 0, range(0, 5)):
    print(even_number)


# Map - Linq.Select. Returns a new element after being passed in the enumerable element
print("\nMap as Squared:")
for n in map(square, range(0, 4)):
    print(n)

print("\nMap as Squared with lambda:")
for n in map(lambda x: x ** 2, range(0, 4)):
    print(n)


# Map can be used for multiple enumerators
print("\nMap Add Two Elements:")
for n in map(add, range(0, 4), range(0, 4)):
    print(n)

print("\nMap Add Two Elements with lambda:")
for n in map(lambda x, y: x + y, range(0, 4), range(0, 4)):
    print(n)

# Map can take lambdas. Here we
print("\nMap as Squared with lambda:")
print(list(map((lambda x: x ** 2), range(0, 4))))

# Reduce: loops through all elements, the input parameter is the return value for the last element.
print("\nReduce")
print(functools.reduce(lambda x, y: x + y, range(4)))  # Starting value of 0. 0 + 1 + 2 + 3
print(functools.reduce(lambda x, y: x + y, range(4), 10))  # Starting value 10. 10 + 1 + 2 + 3
