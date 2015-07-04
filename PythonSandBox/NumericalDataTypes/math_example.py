# math_example.py
#
# Math Example
#
# The math module contains various useful basic maths functions.
#
# There are many third party math modules which should considered where applicable:
#
# SciPy:      http://scipy.org
# NumPy:      http://www.numpy.org/
#
# https://docs.python.org/3.4/library/math.html

import math

# Mathematical Functions
print("\n*** Mathematical Functions")
print("math.ceil(11.11):", math.ceil(11.11))  # Ceiling'
print("math.floor(11.11):", math.floor(11.11))  # Floor
print("math.ceil(-11.11):", math.ceil(-11.11))  # Ceiling'
print("math.floor(-11.11):", math.floor(-11.11))  # Floor

print("min(1,2,3):", min(1, 2, 3))  # Largest argument
print("max(1,2,3):", max(1, 2, 3))  # Smallest argument
print("math.fsum([1, 2, 3]):", math.fsum([1, 2, 3]))  # Sums an enumerable

print("math.modf(1.1):", math.modf(1.1))  # Modf. tuple of real number as integral and fractal
print("math.trunc(1.11):", math.trunc(1.11))  # Truncate
print("math.trunc(-1.11):", math.trunc(-1.11))  # Truncate

print("math.fabs(-999):", math.fabs(-999))  # Abs

print("math.isfinite(1):", math.isfinite(1))  # Not infinite or is finite
print("math.isinf(float('inf')):", math.isinf(float("inf")))  # If infinite
print("math.isnan(float('inf'')):", math.isnan(float("inf")))  # Not NaN

print("math.pow(3, 3):", math.pow(3, 3))  # To the power of
print("math.sqrt(9):", math.sqrt(9))  # Square root

# Trigonometric Functions
print("\n*** Trigonometric Functions")
print("math.radians(360):", math.radians(360))  # Degrees to Radian
print("math.degrees(6.28...):", math.degrees(6.283185307179586))  # Radians to degrees

# acos(x)       Return the arc cosine of x, in radians.
# asin(x)       Return the arc sine of x, in radians.
# atan(x)       Return the arc tangent of x, in radians.
# cos(x)        Return the cosine of x radians.
# hypot(x, y)   Return the Euclidean norm, sqrt(x*x + y*y).
# sin(x)        Return the sine of x radians.
# tan(x)        Return the tangent of x radians.


# Math Constants
print("\n*** Math Constants")
print("math.pi:", math.pi)  # Pi
print("math.e:", math.e)  # E
