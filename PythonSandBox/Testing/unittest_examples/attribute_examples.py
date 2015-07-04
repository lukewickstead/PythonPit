# unittest_examples./assertions_example.py
#
# Example of unittest attributes.
#
# These allow skipping of tests, conditional skipping of tests and declarations of failure.

from unittest import TestCase, skip, skipIf, skipUnless, expectedFailure, SkipTest


class TestAttributes(TestCase):
    @skip("Test is not run")
    def test_skip(self):
        self.fail("This should not be run")

    @skipIf(True, "This is not run")
    def test_skipIf(self):
        self.fail("This should not be run")

    @skipUnless(False, "This is not run")
    def test_skipUnless(self):
        self.fail("This should not be run")

    def test_skipTest(self):
        SkipTest("This should not be run")

    @expectedFailure
    def test_expectedFailure(self):
        self.fail("This is an expected failure")
