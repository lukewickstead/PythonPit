from unittest import TestCase

from ...populations.PopulatePersonByCreate import PopulatePersonByCreate
from ...models import Person


class TestCreateByCreate(TestCase):
    """
    Examples of how to create records with create()
    """

    def setUp(self):
        a_populator = PopulatePersonByCreate()
        a_populator.populate()

    def test_create_by_create(self):
        self.assertEqual(Person.objects.all().count(), 10)
