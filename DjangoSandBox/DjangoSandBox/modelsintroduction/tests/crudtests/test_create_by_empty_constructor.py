from unittest import TestCase

from ...populations.PopulatePersonByEmptyConstructor import PopulatePersonByEmptyConstructor
from ...models import Person


class TestCreateByEmptyConstructor(TestCase):
    """
    Examples of how to create records with an empty constructor call
    """

    def setUp(self):
        a_populator = PopulatePersonByEmptyConstructor()
        a_populator.populate()

    def test_create_by_empty_constructor(self):
        self.assertEqual(Person.objects.all().count(), 10)
