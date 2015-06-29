from unittest import TestCase

from modelsintroduction.populations.PopulatePersonByConstructor import PopulatePersonByConstructor
from modelsintroduction.models import Person


class TestAll(TestCase):
    """
    Examples of how to use all()
    """

    def setUp(self):
        a_populator = PopulatePersonByConstructor()
        a_populator.populate()

    def TestAll(self):
        self.assertEqual(Person.objects.all().count(), 10)

        for a_person in Person.objects.all():
            self.assertIsNotNone(a_person)
