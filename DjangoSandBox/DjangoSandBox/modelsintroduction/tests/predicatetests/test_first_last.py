from unittest import TestCase

from ...populations.PopulatePersonByConstructor import PopulatePersonByConstructor
from ...models import Person


class TestFirstLast(TestCase):
    """
    Examples of how to use first(), last(), latest(), earliest()
    """

    def setUp(self):
        a_populator = PopulatePersonByConstructor()
        a_populator.populate()

    def test_latest(self):
        self.assertEqual(Person.objects.latest("date_of_birth").name, "Dave")

    def test_earliest(self):
        self.assertEqual(Person.objects.earliest("date_of_birth").name, "Jim")

    def test_first(self):
        self.assertEqual(Person.objects.all().order_by("name").first().name, "Charlotte")

    def test_last(self):
        self.assertEqual(Person.objects.all().order_by("name").last().name, "Sophie")
