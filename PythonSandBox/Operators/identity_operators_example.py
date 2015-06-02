# identity_operators_example.py
#
# Identity Operators Example

print("1 is 1:", 1 is 1)
print("1 is 1.0:", 1 is 1.0)
print("1 == 1.0:", 1 == 1.0)

print("1 is not 1:", 1 is not 1)
print("1 is not 1.0:", 1 is not 1.0)

# Tuples are identical when empty but not with identical value type data
print("() is (): ", () is ())
print("(1, 2, 3) is (1, 2, 3): ", (1, 2, 3) is (1, 2, 3))
print("(1, 2, 3) == (1, 2, 3): ", (1, 2, 3) == (1, 2, 3))

# Dictionary and List are never identical
print("[] is []: ", [] is [])
print("{} is {}: ", {} is {})


print("abc" is "abc")