# decimal_example.py
#
# Decimal Example
#
# The decimal type represents a real number ( integral and fraction ) but has a closer representation to the real value.
#
# It is not optimised for computers and as such has a memory and performance hit when compared to floats though they
# are more accurate.
#
# In python decimals can grow to take on more precision and accuracy as required.


from sys import getsizeof
from decimal import Decimal, getcontext

# Assignment is made with the = operator and the decimal constructor
print("\n*** Assignment")
x = Decimal(1.1)

# We can determine the type with the type function
print("\n*** Type")
print(x, type(x))

# We can parse strings to a Decimal including exponential numbers
print("\n*** Passing")
print(Decimal("1"))
print(Decimal("1.0e10"))

# We can round to x d.p
print("\n*** Rounding")
print(round(Decimal(1.111111), 2))

# We can perform many maths operators
# See ../Operators/*.py for more details
print("\n*** Operators")
x = Decimal(1.1)
print(x + x)
print(x - x)
print(x / x)
print(x * x)

print("\n*** Float information")
print(getcontext())

# The memory is always fixed as 104 bytes
print("\n*** Size")
print(getsizeof(Decimal(0)))
print(getsizeof(Decimal(1024)))
print(getsizeof(Decimal(999999999999)))

# Accuracy; provide better accuracy
print("\n*** Accuracy ")
print(.1 + .1 + .1 == .3)
print(Decimal(".1") + Decimal(".1") + Decimal(".1") == Decimal(".3"))
