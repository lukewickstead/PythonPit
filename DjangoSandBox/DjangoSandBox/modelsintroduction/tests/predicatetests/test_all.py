from unittest import TestCase

from ...populations.PopulatePersonByConstructor import PopulatePersonByConstructor
from ...models import Person


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
