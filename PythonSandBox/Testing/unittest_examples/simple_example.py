# unittest_examples/simple_example.py
#
# Simple Unittest Example
#
# All tests can be run with unittest.main() at the terminal.
#
# PyCharm has config settings for which test runner to run a file with

from unittest import TestCase, main


def add_two_numbers(a, b):
    """
    A simple method to test
    """
    return a + b


class MyTestClass(TestCase):
    """
    A simple unit test example
    """

    def test_add_two_numbers(self):
        # self.assertEqual(add_two_numbers(1, 2), 3)
        self.assertEqual(add_two_numbers(1, 2), 4)

if __name__ == '__main__':
    main()
