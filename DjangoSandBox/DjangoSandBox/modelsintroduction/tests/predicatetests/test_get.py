from unittest import TestCase

from django.core.exceptions import ObjectDoesNotExist

from ...populations.PopulatePersonByConstructor import PopulatePersonByConstructor
from ...models import Person, OPTION_SEX_FEMALE


class TestGet(TestCase):
    """
    Examples of how to use get()
    """

    def setUp(self):
        a_populator = PopulatePersonByConstructor()
        a_populator.populate()

    def test_get(self):
        a_person = Person.objects.get(name="Emma")

        self.assertEqual(a_person.name, "Emma")
        self.assertEqual(a_person.sex, OPTION_SEX_FEMALE)
        self.assertEqual(a_person.height, 1.72)

    def test_get_as_failure(self):
        with self.assertRaises(ObjectDoesNotExist):
            Person.objects.get(name="JimmyBob")
