# regular_expressions_example.py
#
# Regular Expressions Example
#
#
# TODO:\b seems to work different from .net
# TODO: Groups don't seem to work the same as in .net
# TODO: Add some more examples

import re

# Luke is matched in Luke Wickstead
match = re.search(r'Luke', 'Luke Wickstead')
if match:
    print(match.group())

# [] defined a set or range of characters to match
# a-z is lower a to lower z inclusive
# A-Z is upper A to upper Z inclusive
match = re.search(r'[a-zA-Z]{4}', 'Luke Wickstead')
if match:
    print(match.group())

# Match a word letter [a-zA-Z0-9_]
# 0-9 is digits 0 to 0 inclusive
# _ is an underscore
# The * is an indefinite range
match = re.search(r'\w*', 'Luke Wickstead')
if match:
    print(match.group())

# {x} defined the number of chars to match
# Here we match 3 upper case letters followed by 3 numbers
match = re.match(r"[A-Z]{3}[0-9]{3}", "ABC123")
if match:
    print(match.group())

match = re.match(r"[A-Z][0-9]", "A1B2C3")
if match:
    print(match.group())
