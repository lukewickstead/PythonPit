# exception_details_example.py
#
# Exception Details Example
#
# Some common information fields on exceptions

try:
    1 / 0
except Exception as err:
    print("Exception: {0}".format(err))
    print(err)
    print(err.__traceback__)
    print(err.args)

