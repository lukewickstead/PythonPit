# lambda_example.py
#
# Lambda Example
#
# Lambdas are inline, anonymous methods.


# Lambda Expression
def square():
    return lambda z: z ** 2


# F is now a function
f = square()
print(f)

# Call as if the function is x.
for x in range(5):
    print("The square of {0} is {1}".format(x, f(x)))


# See list_ordering_example for an example of how to use a lambda as an argument

# Map allows converting an converting a collection into another while providing a map between the
# elements in the old collection and a new one. We can use a lambda expression to achieve this.
print(list(map(lambda y: y ** 2, range(10))))
