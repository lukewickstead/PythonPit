# fraction_example.py
#
# Fraction Example
#
# Represents a fraction; a nominator and a denominator.
#
# A Fraction instance can be constructed from a pair of integers, from another rational number, or from a string.
#

from fractions import Fraction
from decimal import Decimal

# Assignment is made with the = operator and the fraction constructor along with the numerator and a
# denominator as integrals, another fraction or a rational number.

print("\n*** Assignment")
print(Fraction(1, 2))
print(Fraction(Fraction(1, 2)))
print(Fraction(1.1))
print(Fraction(Decimal(1.1)))

# We can determine the type with the type function
print("\n*** Type")
x = Fraction(1, 2)
print(x, type(x))


# We can parse strings rational number into a fraction
print("\n*** Passing")
print(Fraction("1.1"))

# We can perform many maths operators
#  See ../Operators/*.py for more details
print("\n*** Operators")
x = Fraction(1, 2)
print(x + x)
print(x - x)
print(x / x)
print(x * x)
