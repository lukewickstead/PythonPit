# strings_example.py
#
# Strings Example
#
# Strings are immutable

# Can be single or double quotes
print("\n*** Declaration")
print('single quotes')
print('double quotes')

print("\n*** Escaping")
# Prevents having to escape when outputting the string termination!!
print(' " double quotes" ')
print(" ' single quotes' ")

# Can be escaped with \
print(' \' single escaped quotes \' ')
print(" \" double escaped quotes \" ")

# Raw strings disable escaping. Like @ in C#
print(r"This\is\a\raw\string\@ in c#")

# Strings are a collection of characters. Respond to may collection commands
print("\n*** Are Collections of Chars")
a_string = 'HelloWorld!'
print(type(a_string))  # The string class
print(len(a_string))  # The length
print(a_string[0])  # Char at index 0
print(a_string[2:5])  # Chars at index 2 to 5

# Can be duplicated and concatenated
print("\n*** Duplication and Concatenation")
print(a_string + "TEST")  # Concat string
print(a_string * 2)  # String duplicated z10 times

# Multi line strings
print("\n*** Splitting Strings Over Multiple Lines")
print(("This can help"
       " separate Strings"))

print("This can also help  \
separate Strings")

# Str is human readable
# Repr is interpreter readable; allows knowledge of structure
# For example' repr keeps quotes
print("\n*** str vs. repr")
print(repr("Hello"))
print(str("Hello"))


# output with adjustment
print("\n*** Padding")
print("1".rjust(3))
print("1".ljust(3))
print("1".center(3))
print(len("1".center(3)))

print("1".zfill(3))  # zeros to left
