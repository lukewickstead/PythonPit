from unittest import TestCase

from ...populations.PopulatePersonByBulkCreate import PopulatePersonByBulkCreate
from ...models import Person


class TestDeleteModel(TestCase):
    """
    An example of how to delete records.

    """

    def setUp(self):
        a_populator = PopulatePersonByBulkCreate()
        a_populator.populate()

    def test_delete(self):
        a_person = Person.objects.first()
        a_person.save()

        self.assertEqual(Person.objects.all().count(), 10)

        a_person.id = 0
        a_person.name += "1"
        a_person.save()

        self.assertEqual(Person.objects.all().count(), 11)

        a_person.delete()
        self.assertEqual(Person.objects.all().count(), 10)
