from unittest import TestCase

from django.db.models import Avg, Max, Min, Sum, Count

from ...populations.PopulatePersonByConstructor import PopulatePersonByConstructor
from ...models import Person


class TestAggregates(TestCase):
    """
    Examples of how to use aggregate()
    """

    def setUp(self):
        a_populator = PopulatePersonByConstructor()
        a_populator.populate()

    def test_count(self):
        self.assertEqual(Person.objects.count(), 10)
        self.assertEqual(Person.objects.all().aggregate(Count('sex'))["sex__count"], 10)
        self.assertEqual(Person.objects.all().aggregate(Count('sex', True))["sex__count"], 2)

    def test_avg(self):
        self.assertAlmostEqual(Person.objects.all().aggregate(Avg('height'))["height__avg"], 1.73, 2)

    def test_min_and_max(self):
        self.assertEqual(Person.objects.all().aggregate(Max('height'))["height__max"], 1.85)
        self.assertEqual(Person.objects.all().aggregate(Min('height'))["height__min"], 1.55)

    def test_sum(self):
        self.assertAlmostEqual(Person.objects.all().aggregate(Sum('height'))["height__sum"], 17.3, 2)

    def test_distinct(self):
        with self.assertRaises(NotImplementedError):
            self.assertEqual(Person.objects.all().distinct("sex").count(), 2)
