# function_documentation_example.py
#
# Function Documentation Example

# Comments / Documentation


def my_function(a, *b, **c):
    """
    This does not really do anything,
    but it it did it would be the best function in the world
    :param a: a is the
    :param b: b to the b
    :param c: c from the run dm
    :return: Not much
    """
    print(a, b, c)


print("*** __doc__")
print(my_function.__doc__)

print("\n*** help(my_function)")
help(my_function)
