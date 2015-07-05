from unittest import TestCase

from ...populations.populate_man_and_dog import populate
from ...models import Man, Dog


class TestOneToOne(TestCase):
    """
    Examples of how to create parent and children records who are joined with a 1:1 (One to One) join.
    """

    def setUp(self):
        populate()

    def test_one_to_one(self):
        self.assertEqual(Man.objects.all().count(), 3)
        self.assertEqual(Dog.objects.all().count(), 3)

    def test_parent_to_child(self):
        self.assertEqual(Man.objects.get(name="Luke").dog.name, "Fido")

        a_dog = Dog.objects.get(name="Fido")
        self.assertEqual(Man.objects.get(dog=a_dog).name, "Luke")

    def test_child_to_parent(self):
        self.assertEqual(Dog.objects.get(name="Fido").owner.name, "Luke")

        a_man = Man.objects.get(name="Luke")
        self.assertEqual(Dog.objects.get(owner=a_man).name, "Fido")
