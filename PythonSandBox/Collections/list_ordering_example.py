# list_ordering_example.py
#
# List Ordering Example
#
# See ControlFlow/loops_example.py

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Raw Data:", numbers)

# Reverse
numbers.reverse()
print("Reversed: ", numbers)

# Sort
numbers.sort()
print("Sorted: ", numbers)

# Sort with Lambda
print("\nSorted With Lambda")
named_numbers = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print("Raw Data:", named_numbers)

named_numbers.sort(key=lambda pair: pair[0])
print("Sorted With Pair[0]:", named_numbers)

named_numbers.sort(key=lambda pair: pair[1])
print("Sorted With Pair[1]:", named_numbers)
