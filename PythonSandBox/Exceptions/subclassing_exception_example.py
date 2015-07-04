# subclassing_exception_example.py
#
# Subclassing Exception Example
#
# Create a new class inheriting from Exception or a Class which inherits from Exception
# Only classes with Exception in their ancestry can be thrown


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2 * 2)
except MyError as e:
    print(e.value)
    print(e)
