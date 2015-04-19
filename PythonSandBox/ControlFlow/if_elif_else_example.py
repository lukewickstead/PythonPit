# if_elif_else_example.py
#
# If Elif Else Example


def print_condition(value):
    if value < 1:
        print("@If")
    elif value == 1:
        print("@Else IF")
    else:
        print("@Else")

for x in range(3):
    print_condition(x)