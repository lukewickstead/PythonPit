# try_finally_example.py
#
# Finally statement is run even if am exception is thrown and caught or thrown and not caught.


def raise_if_true(arg_input):
    try:
        if arg_input == 1:
            raise ValueError("Input was 1")
        elif arg_input == 2:
            raise Exception("Input was 2")
    except ValueError as exception:
        print("Caught:", exception)
    finally:
        print('This is the finally!!!!')

for number in [1, 2, 3]:
    raise_if_true(number)