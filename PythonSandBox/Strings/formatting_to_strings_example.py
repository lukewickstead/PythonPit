# formatting_to_strings_example.py
#
# Formatting To Strings Example
#
# Helpful functionality when outputting data to strings

# Concatenating with template holders
print("\n*** Concatenating with template holders")
print('{0} can have {1} templates or placeholders'.format('Strings', 'ordinal'))
print('{first} can have {second} templates or placeholders'.format(first='Strings', second='named'))
print('{0} and {named} placeholders can be mixed!'.format('Ordinal', named='named'))

# Concatenating with key value pairs as template holders
print("\n*** Concatenating with KVP")
data_table = {'One': 'And a one!', 'Two': 'And a two!'}
print(type(data_table), data_table)
print('One: {0[One]:s}; Two: {0[Two]:s}'.format(data_table))
print('One: {One:s}; Two: {Two:s}'.format(**data_table))  # With Unpacking

# Older versions of python used implicit ordinal positions
print("\n*** Old School")
print("Hello there %s %s %s" % ("Mr", "Luke", "Wickstead"))

# Format Specification Mini-Language
print("\n*** Format Specification Mini-Language")

# Formatting Floats
# Format        Description
# {:.<x>f}      Format to x decimal places
# {:+.<x>f}	    Format to x decimal places with +/- sign
print("\n*** Formatting Floats")
print("{0:.0f}".format(123.456))  # 0 dp
print("{0:.2f}".format(123.456))  # 2 dp
print("{0: 8.3f}".format(123.456))  # 3 dp with padding to 8 chars
print("{0:+.3f}".format(123.456))  # 3 dp with +/-
print("{0:-.3f}".format(-123.456))  # 3 dp with - if -ve.


# Number Separator
# Format        Description
# {:,}          Format a number with y separator
print("\n*** Number Separator")
print("{0:,}".format(-1121212123.456))  # , (comma) separator

# Space Padding / Alignment
# Format        Description
# {:<y>><x>d}	Left pad with char y to a total of x characters
# {:<y><<x>d}	Right pad with char y to a total of x characters
# {:<y>^<x>d}	Centre pad with char y to a total of x characters
# {:<x>d}	    Left space pad to a total of x characters in length
# {:<<x>d}	    Right space pad with <x> characters in length
# {:^<x>d}	    Center space pad to a total of x characters in length

print("\n*** Space Padding / Alignment")
print("{0:0>5d}".format(1))  # Left pad with 0 to 5 chars
print("{0:0<5d}".format(1))  # Right pad with 0 to 5 chars
print("{0:0^5d}".format(1))  # Centre pad with 0 to 5 chars
print("{0:5d}".format(1))  # Left pad with space to 5 chars
print("{0:<5d}".format(1))  # Right pad with space to 5 chars
print("{0:^5d}".format(1))  # Centre pad with space to 5 chars

# Percentages
# Format        Description
# {:.<x>%}	    Format a percentage to x dp
print("\n*** Formatting Percentages")
print("{0:.3%}".format(0.25555))  # Format percentage to 3dp


# The Format Specification Mini-Language Specification
print("\n*** More On Format Specification Mini-Language")
# https://docs.python.org/2/library/string.html

# Format      Description
# format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
# fill        ::=  <any character>
# align       ::=  "<" | ">" | "=" | "^"  (Left, right, after sign, center
# sign        ::=  "+" | "-" | " " (+ is always use sign. - is only for -ve numbers. space is space for + and - for -ve.
# #           ::= Formats binary, octal or hex numbers prefixed with '0b', '0o', or '0x',
# 0           ::= Enable sign aware zero padding of the width.
# width       ::=  integer
# precision   ::=  integer
# type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

# types
# s     = string
# b     = binary
# c     = character
# d     = Decimal ( base 10 ) integer
# o     = octal
# x/X   = hex
# n     = number. Uses computer config to determine localisation ( eg , or . separator )
# none  = d
# e/E   = exponential
# g/G   = general, provides general rules for precision, rounding and when a max number before switching to exponential
# %     = percentage

print("{0:g}".format(1111123.456))  # As general
print("{0:5.2n}".format(123.456))  # As number
print("{0:b}".format(123))  # As Binary
print("{0:x}".format(123))  # As hex
print("{0:e}".format(123))  # As exponential
