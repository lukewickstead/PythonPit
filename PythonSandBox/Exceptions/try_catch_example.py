# try_catch_example.py
#
# Example of try and catch.


def convert_to_int(input_value):
    try:
        x = int(input_value)
        print("{0} can be converted into an int of {1}".format(input_value, x))
    except ValueError as exception:
        print("The following exception was caught:")
        print(exception)

for an_input in ["1", "a", "b"]:
    print("\nTrying with:", an_input)
    convert_to_int(an_input)