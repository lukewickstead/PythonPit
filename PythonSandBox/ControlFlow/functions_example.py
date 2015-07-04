# functions_example.py
#
# Functions Example
#


def no_argument_method():
    print("NoArgument")


def argument_method(a):
    print("Argument({0})".format(a))


def optional_argument_method(a="A Default Value"):
    print("OptionalArgument({0})".format(a))


print("*** Method And Argument Definitions")
no_argument_method()
argument_method("Bang!!!")
optional_argument_method()
optional_argument_method("Bang!!!")

print("\n*** Default Arguments As Variables")
# Default values are evaluated when the function is defined. Here x is 5 when the method is compiled, therefore arg
# will always be 5, regardless of the value of x during runtime.

x = 5


def optional_argument_as_a_variable(arg=x):
    global x
    print("x = {0}, arg = {1}".format(x, arg))


x = 6
optional_argument_as_a_variable()

print("\n*** Default Arguments As A Reference Type")

# Reiterating the point, this is the same for mutable types; they are only ever created once.
# Here we assign a list as default value. Every time the method is called without a new_list argument the method is
# passed in the same list instance which is created during runtime.


# noinspection PyDefaultArgument
def optional_argument_as_a_new_list(to_append, new_list=[]):
    new_list.append(to_append)
    return new_list


for x in range(4):
    print(optional_argument_as_a_new_list(x))

print("\n*** Default Arguments As Value Types")
# Default parameters are evaluated only once.
# Here the value type is immutable and hence is always defaulted to 1 no matter how many times it is incremented


def increment_optional_argument(a=1):
    a += 1
    return a


for x in range(3):
    print(increment_optional_argument())

print("\n*** Named Arguments")
# All optional arguments can be called by name after all mandatory arguments


def named_arguments(a, b=2, c=3):
    print("A: {0}, B: {1}, C: {2}".format(a, b, c))


named_arguments(2, c=1)

print("\n*** * and ** arguments")
# * Is all remaining arguments passed in as a tuple
# ** Collects named arguments in a dictionary


def star_and_star_star_method(name, *children, **characteristics):
    print("Name:", name, type(name))
    print("Children:", children, (type(children)))
    print("Characteristics:", characteristics, type(characteristics))


star_and_star_star_method("Luke", "Jim,", "Bob", hair="Fair", height="Tall")

# Dictionary can be unpacked into named parameters
print("\n*** ** unpacked from a dictionary")

star_and_star_star_method("Luke", "Jim,", "Bob", **{"hair": "Fair", "height": "Tall"})
