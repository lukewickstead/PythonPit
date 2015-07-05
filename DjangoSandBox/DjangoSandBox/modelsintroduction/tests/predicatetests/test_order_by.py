from unittest import TestCase

from ...populations.PopulatePersonByConstructor import PopulatePersonByConstructor
from ...models import Person


class TestOrderBy(TestCase):
    """
    Examples of how to use order_by()
    """

    def setUp(self):
        a_populator = PopulatePersonByConstructor()
        a_populator.populate()

    def test_order_by(self):
        last_height = 0
        people_by_height = Person.objects.all().order_by("height")

        for a_person in people_by_height:
            self.assertLessEqual(last_height, a_person.height)
            last_height = a_person.height

        self.assertEqual(people_by_height.first().name, "Sophie")
        self.assertEqual(people_by_height.last().name, "John")

    def test_reverse_by(self):
        people_by_height_desc = Person.objects.all().order_by("height").reverse()
        self.assertEqual(people_by_height_desc.last().name, "Sophie")
        self.assertEqual(people_by_height_desc.first().name, "John")
