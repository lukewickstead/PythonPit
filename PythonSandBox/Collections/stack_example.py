# stack_example.py
#
# Stack Example
#
# Last In First Out

numbers = []

for x in range(10):
    numbers.append(x)

# Remove last element
print(numbers.pop())

# Remove element at index x
print(numbers.pop(3))