from unittest import TestCase

from ...populations.PopulatePersonByConstructor import PopulatePersonByConstructor
from ...models import Person


class TestCreateByConstructor(TestCase):
    """
    Examples of how to create records with the constructor call
    """

    def setUp(self):
        a_populator = PopulatePersonByConstructor()
        a_populator.populate()

    def test_create_by_constructor(self):
        self.assertEqual(Person.objects.all().count(), 10)
