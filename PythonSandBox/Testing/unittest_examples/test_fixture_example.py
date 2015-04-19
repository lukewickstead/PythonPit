# unittest_examples./test_fixture_example.py
#
# Example of UnitTest Test Fixture Example

from unittest import TestCase


class TestFixtureExample(TestCase):

    def setUp(self):
        # Set up / initialise before a test
        # If this fails then no tests will be run
        print("In the setUp")

    def tearDown(self):
        # Destroy any resources required during the test
        # Will always be run if setUp runs regardless of tests successes
        print("In the tearDown")

    def test_fixture(self):
        self.assertTrue(True)