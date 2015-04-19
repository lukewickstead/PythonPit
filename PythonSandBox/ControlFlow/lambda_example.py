# lambda_example.py
#
# Lambda Example
#
# Lambdas are inline, anonymous methods.

# Lambda Expression
def Square():
    return lambda x: x**2

# F is now a function
f = Square()
print(f)

# Call as if the function is x.
for x in range(5):
    print("The square of {0} is {1}".format(x, f(x)))