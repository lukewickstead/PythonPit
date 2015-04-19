# operator_precedence_example.py
#
#  Operator Precedence Example

# Operators higher up the table have a higher precedence
# Operators on the same row and to the left have a higher precedence

# Operator	                    Description
#  **	                        Exponential ( to the power of )
# ~ + -	                        Bitwise not, unary add ( +ve ) and subtract (-ve) ( +1, -1 )
# * / % //	                    Multiplication, division and modulus and floor division
# + -	                        Addition and subtraction
# >> <<	                        Bitwise shift right and left
# &	                            Bitwise and
# ^ |	                        Bitwise xor and or
# <= < > >=	                    Comparison operators
# <> == !=	                    Equality operators
# = %= /= //= -= += *= **=	    Assignment operators
# is is not	                    Identity operators
# in not in	                    Membership operators
# not or and	                Logical operators


# It is bad practice to rely on operator precedence.
# Use brackets which increases code reliability
# ( 1 + (2 * 3)  = 1 + 2 * 3
print(1 + (2 * 3),  1 + 2 * 3)