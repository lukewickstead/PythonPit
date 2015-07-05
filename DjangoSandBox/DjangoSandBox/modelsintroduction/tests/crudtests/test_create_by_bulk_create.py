from unittest import TestCase

from ...populations.PopulatePersonByBulkCreate import PopulatePersonByBulkCreate
from ...models import Person


class TestCreateByBulkCreate(TestCase):
    """
    Examples of how to create records with bulk_create()
    """

    def setUp(self):
        a_populator = PopulatePersonByBulkCreate()
        a_populator.populate()

    def test_create_by_bulk_create(self):
        self.assertEqual(Person.objects.all().count(), 10)
