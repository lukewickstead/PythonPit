# try_catch_else_finally.py
#
# Try Catch Else Finally
#
# Else runs if an exception was not caught
# Finally runs regardless if an exception was caught or not.


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


print("1/2:")
divide(1, 2)

print("\n1/0:")
divide(1, 0)
