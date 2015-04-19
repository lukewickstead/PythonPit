# doc_test_example.py
#
# Doc Test Example
#
# Doc Test allows testing of code where an example is provided within a documentation header


def add_two_numbers(value_one, value_two):
    """Adds two numbers together.

    >>> print(add_two_numbers(1, 99))
    100
    """
    return value_one + value_one + value_two  # intentional error to show failed test

# This would be placed somewhere else
import doctest

doctest.testmod()  # automatically validate the embedded tests