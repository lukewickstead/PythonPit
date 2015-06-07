# loops_example.py
#
# Loops Example

# Iterate through an innumerable via its enumerator

print("*** For In Loop")
for number in [1, 2, 3]:
    print(number)

# This loops through a copy allowing you to edit the original without issues
print("\n*** For In Loop With Shallow Copy")

letters = ['a', 'b', 'c']
for letter in letters[:]:
    letters.append(letter)

print(letters)

# Enumerate returns the index and the element
print("\n*** For Loop With enumerate()")

for index, letter in enumerate(letters[:]):
    print("{0} => {1}".format(index, letter))

# Range allows easy looping over a range
print("\n*** For Loop With range()")
for number in range(10, 20, 3):  # start, stop, step
    print(number)

# Backwards for elements in a descending order
# for number in range(3, 0, -1):  # start, stop, step

# Only works for integers; the following causes a traceback
# for number in range(0.1, 0.2, 0.01):  # start, stop, step

# Break, Continue and Else
print("\n*** Break, Continue & Else")
for number in range(10):  # 0-9
    if number == 0:
        print(number, "continue")
        continue
    print(number, "break")
    break
else:
    print("else")  # Always runs unless the loop is terminated with a break

print("\n*** Break, Continue & Else 2nd")
for number in range(10):  # 0-9
    if number == 0:
        print(number, "continue")
        continue
else:
    print("else")  # Always runs unless the loop is terminated with a break


# Iterate through multiple enumerable at the same time
print("\n*** zip ")
numbers = [1, 2, 3]
words = ['one', 'two', 'three']
letters = ['a', 'b']
for number, word, letter in zip(numbers, words, letters):
    print('{0} => {1} => {2}'.format(number, word, letter))

# Reverse an enumerator
print('\n*** Reversed')
for i in reversed(range(1, 10, 2)):
    print(i)

# Sort an numerator
print("\n*** Sorted ")
for f in sorted((5, 2, 3, 7, 6)):
    print(f)

# Sort an numerator
print("\n*** Sorted Reversed ")
for f in sorted((5, 2, 3, 7, 6), reverse=True):
    print(f)

# Key Value Pair Iteration
print("\n*** Key Value Pair Iteration")
for k, v in {'one': 1, 'two': 2}.items():
    print(k, v)