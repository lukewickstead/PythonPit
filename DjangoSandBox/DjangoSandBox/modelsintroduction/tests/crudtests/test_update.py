from unittest import TestCase

from modelsintroduction.models import Person, OPTION_SEX_FEMALE, OPTION_SEX_MALE
from modelsintroduction.populations.PopulatePersonByConstructor import PopulatePersonByConstructor


class TestUpdate(TestCase):
    """
    Examples of how to use update() to bulk update records or individually with the save() function
    """

    def setUp(self):
        a_populator = PopulatePersonByConstructor()
        a_populator.populate()

    def test_group_update(self):
        Person.objects.filter(sex=OPTION_SEX_FEMALE).update(validated=True)

        self.assertEqual(Person.objects.filter(sex=OPTION_SEX_FEMALE, validated=True).count(), 5)

    def test_update(self):
        tallest_man = Person.objects.filter(sex=OPTION_SEX_MALE).order_by("height").reverse().first()

        tallest_man.validated = True
        tallest_man.save()

        self.assertEqual(Person.objects.filter(sex=OPTION_SEX_MALE).order_by("height").first().validated, False)
        self.assertEqual(Person.objects.filter(sex=OPTION_SEX_MALE).order_by("height").last().validated, True)
