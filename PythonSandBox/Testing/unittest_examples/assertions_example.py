# unittest_examples./assertions_example.py
#
# Example of unittest assertions


from unittest import TestCase
from warnings import warn


class TestAssertsExample(TestCase):
    """
    Examples of how to use all the assert methods
    """

    def test_demo_asserts(self):
        # Equality
        self.assertEqual(1, 1)
        self.assertEqual(1.0, 1)
        self.assertNotEqual(1, 2)
        self.assertAlmostEqual(1.1, 1.11, 1)  # 3rd argument is the precession
        self.assertNotAlmostEqual(1.1, 1.11, 2)  # 3rd argument is the precession

        # AssertEqual can provide an equality check most types
        self.assertEqual([1, 2, 3], [1, 2, 3])
        self.assertEqual((1, 2, 3), (1, 2, 3))
        self.assertEqual({1, 2, 3}, {1, 2, 3})
        self.assertEqual({'a': 1}, {'a': 1})
        self.assertEqual("one\ntwo", "one\ntwo")

        # Assert Equals Implicitly Calls (prefer assertEqual)
        self.assertListEqual([1, 2, 3], [1, 2, 3])
        self.assertTupleEqual((1, 2, 3), (1, 2, 3))
        self.assertSetEqual({1, 2, 3}, {1, 2, 3})
        self.assertDictEqual({'a': 1}, {'a': 1})
        self.assertMultiLineEqual("one\ntwo", "one\ntwo")

        # Boolean
        self.assertFalse(False, "False is not false!")
        self.assertTrue(True)

        # Collections
        self.assertSequenceEqual((1.0, 2.0, 3.0), [1, 2, 3])  # Checks only the sequence
        self.assertEqual([1.0, 2.0, 3.0], [1, 2, 3])  # Can be used with many types.
        self.assertIn(1, (1, 2, 3))
        self.assertNotIn(4, (1, 2, 3))
        self.assertCountEqual((1, 2, 3), (3, 2, 1))  # Badly named. This checked elements and not their order

        # Comparison
        self.assertLess(1, 10)
        self.assertLessEqual(1, 1)
        self.assertGreater(10, 1)
        self.assertGreaterEqual(1, 1)

        # Identity
        self.assertIs(1, 1)
        self.assertIsNot(1, 2)
        self.assertIsNone(None)
        self.assertIsNotNone(1)
        self.assertIsInstance((), tuple)
        self.assertNotIsInstance((), set)

        # Regular Expression
        self.assertRegex('Luke', "^[a-zA-Z]{3,4}$")
        self.assertNotRegex('Lukey', "^[a-zA-Z]{3,4}$")

        # Exception
        with self.assertRaises(ZeroDivisionError) as ex:
            print(1 / 0)

        self.assertEqual(str(ex.exception), "division by zero")
        self.assertIsInstance(ex.exception, ZeroDivisionError)

        with self.assertRaisesRegex(ZeroDivisionError, "^division by [a-zA-z]{4}$"):
            print(1 / 0)

        # Warnings
        with self.assertWarns(DeprecationWarning) as wn:
            warn("deprecated", DeprecationWarning)

        self.assertEqual(str(wn.warning), "deprecated")

        with self.assertWarnsRegex(DeprecationWarning, "^deprecate[a-z]$"):
            warn("deprecated", DeprecationWarning)
