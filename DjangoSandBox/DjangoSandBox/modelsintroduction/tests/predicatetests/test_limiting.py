from unittest import TestCase

from modelsintroduction.models import Person
from modelsintroduction.populations.PopulatePersonByConstructor import PopulatePersonByConstructor


class TestLimiting(TestCase):
    """
    Examples of how to use list slicing to limit the data returned.
    """

    def setUp(self):
        a_populator = PopulatePersonByConstructor()
        a_populator.populate()

    def test_limiting_to_top_two(self):
        # This is the same as using OFFSET/LIMIT
        self.assertEqual(Person.objects.all().order_by("name")[1:3].count(), 2)

    def test_limiting_to_first(self):
        # Gets the first entry
        self.assertEqual(Person.objects.all().order_by("name")[0].name, "Charlotte")
