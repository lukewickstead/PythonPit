# list_comprehensions_example.py
#
# List Comprehensions Example.py
#
# Allows the generation of a list of elements from input enumerator/enumerable data
# An optional conditional predicate

# The square of the numbers [0-9] is used with the range enumerator
print([x ** 2 for x in range(10)])

# The square of the numbers [0-9] but using map/lambda
print(list(map(lambda x: x ** 2, range(10))))

# Where multiple enumerators are provided a nested loop is provided;
# every combination of elements is used to generate the list

print("\n*** Nested For In")
print([(x, y) for x in [1, 2, 3] for y in [10, 11, 12]])  # All combinations of elements

print("\n*** Zip")
print([(x, y) for x, y in zip([1, 2, 3], [10, 11, 12])])  # All pairs at the same ordinal position.
print([(x, y) for x, y in zip([1, 2, 3], [10, 11, 12, 13])])  # Only elements matched will be iterated through.

# Here we restrict x from being even
print("\n*** If")
print([(x, y) for x in [1, 2, 3] for y in [10, 11, 12] if x % 2 == 0 & y % 2 == 0])

# All letters in abcdef whihc are not in cab
print("\n*** Not In")
print({x for x in 'abcdef' if x not in 'cab'})