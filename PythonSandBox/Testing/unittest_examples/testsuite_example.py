# unittest_examples./testsuite_example.py
#
# Example of unittest TestSuite
#
# You can register required tests to be run via the TextTaskRunner


from unittest import TestSuite, TextTestRunner, TestLoader

from Testing.unittest_examples.simple_example import MyTestClass
from Testing.unittest_examples.assertions_example import TestAssertsExample


# Test Suite
def my_test_suite():
    suite_one = TestSuite()
    suite_one.addTest(MyTestClass('test_add_two_numbers'))

    suite_two = TestLoader().loadTestsFromTestCase(TestAssertsExample)

    return TestSuite([suite_one, suite_two])


# Run the test suite
if __name__ == '__main__':
    TextTestRunner().run(my_test_suite())
