from unittest import TestCase

from ...populations.populate_man_and_dog import populate
from ...models import Man, Dog


class TestCreateAuthorBook(TestCase):
    """
    Examples of how to create parent and children records who are joined with a 1:1 (One to One) join.
    """

    def setUp(self):
        populate()

    def test_create_man_dog(self):
        self.assertEqual(Man.objects.all().count(), 3)
        self.assertEqual(Dog.objects.all().count(), 3)
