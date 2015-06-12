# complex_example.py
#
# Complex Example
#
# Complex numbers have a real and imaginary part both of which which are floating point numbers.


# Assignment is made with the = operator and the complex constructor
print("\n*** Assignment")
x = complex(1.1, 2.2)

# We can determine the type with the type function
print("\n*** Type")
print(x, type(x))

# We can perform many maths operators
#  See ../Operators/*.py for more details
print("\n*** Operators")
x = complex(1.1, 2.2)
print(x + x)
print(x - x)
print(x / x)
print(x * x)
