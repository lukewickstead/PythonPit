# Although there is no built-in method for copying model instances,
# it is possible to easily create new instance with all fields’ values copied.
# In the simplest case, you can just set pk to None. Using our blog example:


from unittest import TestCase

from modelsintroduction.populations.PopulatePersonByBulkCreate import PopulatePersonByBulkCreate
from modelsintroduction.models import Person


class TestCopyModel(TestCase):
    """
    We cannot clone a Model itself but we can reset the PK and save to mimic a clone or copy of a model.

    """

    def setUp(self):
        a_populator = PopulatePersonByBulkCreate()
        a_populator.populate()

    def test_copy(self):
        a_person = Person.objects.first()
        a_person.save()

        self.assertEqual(Person.objects.all().count(), 10)

        a_person.id = 0
        a_person.name += "1"
        a_person.save()

        self.assertEqual(Person.objects.all().count(), 11)

        a_person.delete()
