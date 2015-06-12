# glob_example.py
#
# Glob Example
#
# Glob provides functionality for getting a list of files on a hard disk.
#
# The pattern rules for glob are not actually regular expressions but standard Unix path expansion rules.
#
# * matches zero or more characters as wild card characters
# ? matches a single character as wild card character
# [] matches a range of characters. - implies a range of possibilities
#   [0123456789] matches any number
#   [abc] matches letters a, b or c as lowercase letters
#   [0-9] matches any number
#   [a-zA-Z] matches any letter upper or lowercase
#   [!abc] matches anything except letters a, b or c
#
# The search is local to the define directory and it not recursive. TYou can use os.walk
# in combination to produce recursive searching.


from glob import glob

print("*** Finding glob*.*")
for name in glob('glob*.*'):
    print(name)

print("*** Finding *.txt")
for name in glob('*.txt'):
    print(name)

print("*** Finding ?og.txt")
for name in glob('?og.txt'):
    print(name)

print("*** Finding [a-z]og.txt")
for name in glob('[a-z]og.txt'):
    print(name)

print("*** Finding [!abcde]og.txt")
for name in glob('[!abcde]og.txt'):
    print(name)
