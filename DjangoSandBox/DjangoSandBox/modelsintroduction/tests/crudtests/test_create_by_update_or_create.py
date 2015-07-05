from unittest import TestCase

from ...populations.PopulatePersonByUpdateOrCreate import PopulatePersonByUpdateOrCreate
from ...models import Person


class TestCreateByUpdaterCreate(TestCase):
    """
    Examples of how to create records with update_or_create()
    """

    def setUp(self):
        a_populator = PopulatePersonByUpdateOrCreate()
        a_populator.populate()

    def test_create_by_update_or_create(self):
        self.assertEqual(Person.objects.all().count(), 10)
