# try_catch_else_finally.py
#
# Try Catch Else Finally
#
# Else runs if an exception was not caught
# Finally runs regardless if an exception was caught or not.


def divide(x, y):
    try:
        print("\nPerforming: {0} / {1}".format(x, y))
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("Result =", result)
    finally:
        print("Executing the finally clause")

divide(1, 2)
divide(1, 0)
