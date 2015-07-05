from unittest import TestCase

from ...populations.PopulatePersonByGetOrCreate import PopulatePersonByGetOrCreate
from ...models import Person


class TestCreateByGetOrCreate(TestCase):
    """
    Examples of how to create records with get_or_create()
    """

    def setUp(self):
        a_populator = PopulatePersonByGetOrCreate()
        a_populator.populate()

    def test_create_by_get_or_create(self):
        self.assertEqual(Person.objects.all().count(), 10)
