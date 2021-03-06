# list_example.py
#
# List Example

# Lists are mutable and dynamic. They can contain heterogeneous objects.

# [] is used to initialise

print("*** Initialise")

numbers = []
print(type(numbers), numbers)

numbers = [1, 2, "three", 4]
more = [5, 'six', 7, 8]

print(type(numbers), numbers)
print(numbers, more)

# Elements are referenced nu their index or ordinal position starting at 0
print("\n*** Basic Information")
print("numbers[0]:", numbers[0])
# print("numbers[10]:", numbers[10])
print("numbers.index('three'):", numbers.index('three'))  # Index of element by value
# print("numbers.index('nine'):", numbers.index('nine'))  # Index of element by value
print("'three' in numbers: ", 'three' in numbers)
print("'nine' not in numbers: ", 'nine' not in numbers)
print("len(numbers):", len(numbers))  # List Length


# Nested lists
print("\n*** Nested Lists")
print("Nested Lists:", [[1], [1, 2], [1, 2, 3]])

# Modifying
print("\n*** Modifying Lists")

# Append one element
numbers.append(9)
print("numbers.append(9):", numbers)

# Append multiple elements
numbers.extend([10, 11])
print("numbers.extend([10,11]):", numbers)

# Insert element into an index
numbers.insert(12, 99999)
print("numbers.insert(12, 99999):", numbers)

# Remove element at an index
numbers.remove(10)
print("numbers.remove(10):", numbers)

# Lists can be concatenated
numbers = [1, 2, "three", 4]
more = [5, 'six', 7, 8]
print("numbers + more:", numbers + more)

# Lists can be duplicated
numbers = [1]
print("numbers * 5:", numbers * 5)

# Sequence comparison compares elements at the same ordinal position
# Modifying
print('\n*** List Conditional Operators')

# Compares each element at the same ordinal position
print("1, 2, 5) >= (1, 2, 5):", (1, 2, 5) >= (1, 2, 5))

# Checks each element for equality
print("(1,2) == (1.0, 2.0):", (1, 2) == (1.0, 2.0))

# Can be used for most immutable elements
print('("a","b") < ("e", "f"):', ("a", "b") < ("e", "f"))


# Counts the number of instances of an element.
print('\n*** Count')
print([1, 2, 1].count(1))
