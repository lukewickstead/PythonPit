# bitwise_operators_example.py
#
# Bitwise Operators Example

one = 111
two = 333

print('one: {0:b}'.format(one))
print('two: {0:b}'.format(two))


# & = Each bit at the same ordinal position are performed AND operator
print('{0:b} & {1:b} = {2:b}'.format(one, two, one & two))

# | = Each bit at the same ordinal position are performed OR operator
print('{0:b} | {1:b} = {2:b}'.format(one, two, one | two))

# ^ = Each bit at the same ordinal position are performed XOR operator. XOR is OR but not Both
print('{0:b} ^ {1:b} = {2:b}'.format(one, two, one ^ two))

# ~ = Bitwise inversion. Each bit is flipped. 0 -> 1 and 1 -> 0
print('~{0:b} = {1:b}'.format(one, ~one))

# >> = Bitwise shift right. Bits all move to the right x places. First x bits are truncated
print('{0:b} >> 2 = {1:b}'.format(one, one >> 2))

# << = Bitwise shift left. Bits all move to the left x place. First x bits become 0's
print('{0:b} << 2 = {1:b}'.format(one, one << 2))
