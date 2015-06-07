# numbers_example.py
#
# Numbers Example

# There are five types of numbers: int, float, decimal, fraction and complex numbers

from decimal import Decimal
from fractions import Fraction


def print_type(input_value):
    print("The type of", input_value, "is", type(input_value))


# int, float, decimal fraction, complex
for a_number in [1, 1.1, Decimal(1.1), Fraction(1, 2), complex(-1.0, 0.0)]:
    print_type(a_number)

# Round can be used to upon numbers
print("round(1.111111, 2) =", round(1.111111, 2))   # Round to x dp