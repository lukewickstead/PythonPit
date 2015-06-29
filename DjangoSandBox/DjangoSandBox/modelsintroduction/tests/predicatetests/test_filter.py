from unittest import TestCase

from django.db.models import Q, F
from modelsintroduction.populations.PopulatePersonByConstructor import PopulatePersonByConstructor
from modelsintroduction.models import Person, OPTION_SEX_FEMALE, OPTION_SEX_MALE

# Reference:
# https://docs.djangoproject.com/en/1.8/ref/models/querysets
# https://docs.djangoproject.com/en/1.8/topics/db/queries
# https://docs.djangoproject.com/en/1.8/ref/models/lookups


class TestFilter(TestCase):
    """
    Examples of how to use filter()

    Filter() returns a QuerySet which can be used to predicate or search upon the data contained within the database.

    Each QuerySet returned is unique; you can save them and use them.

    QuerySet's are lazy; they never hit the database until they need the data.

    Queries are cached upon the QuerySet; the cache is favoured over going to the database as this will be quicker

    Only when accessing the data directly will the db/cache be touched to return the data. Calling filter() itself
    does not access the data, in fact you can chain filter() to separate logic.
        https://docs.djangoproject.com/en/1.8/ref/models/querysets/#when-querysets-are-evaluated

    If you pass an invalid keyword argument into filter() a TypeError is raised.

    """

    def setUp(self):
        a_populator = PopulatePersonByConstructor()
        a_populator.populate()

    def test_predicates(self):
        # Querying a field directly is made by the <name>__exact keyword. A shortcut is to use <name>.
        self.assertEqual(Person.objects.filter(id=1).count(), 1)
        self.assertEqual(Person.objects.filter(id__exact=1).count(), 1)

        # PK can be used to hit the primary key field directly which will be id/id__exact as default
        self.assertEqual(Person.objects.filter(pk=1).count(), 1)

        self.assertEqual(Person.objects.filter(name__exact="Sophie").count(), 1)
        self.assertEqual(Person.objects.filter(name__iexact="sophie").count(), 1)

        self.assertEqual(Person.objects.filter(name__isnull=False).count(), 10)
        self.assertEqual(Person.objects.filter(name__isnull=True).count(), 0)

    def test_string_predicates(self):
        self.assertEqual(Person.objects.filter(name__contains="Sop").count(), 1)
        self.assertEqual(Person.objects.filter(name__icontains="sop").count(), 1)

        self.assertEqual(Person.objects.filter(name__regex="^[SJ]").count(), 4)
        self.assertEqual(Person.objects.filter(name__iregex="^[sj]").count(), 4)

        self.assertEqual(Person.objects.filter(name__startswith="Sop").count(), 1)
        self.assertEqual(Person.objects.filter(name__endswith="hie").count(), 1)

        self.assertEqual(Person.objects.filter(name__istartswith="sop").count(), 1)
        self.assertEqual(Person.objects.filter(name__iendswith="hie").count(), 1)

        # SQLite3 does not support full-text search
        with self.assertRaises(NotImplementedError):
            self.assertEqual(Person.objects.filter(name__search="sop").count(), 1)

    def test_dates_predicates(self):
        # also hour, min, second, week_day
        self.assertEqual(Person.objects.filter(date_of_birth__year=1977).count(), 1)
        self.assertEqual(Person.objects.filter(date_of_birth__month=8).count(), 2)
        self.assertEqual(Person.objects.filter(date_of_birth__day=25).count(), 1)

    def test_choices_and_in_predicates(self):
        self.assertEqual(Person.objects.filter(sex=OPTION_SEX_FEMALE).count(), 5)
        self.assertEqual(Person.objects.filter(sex=OPTION_SEX_FEMALE).first().sex, "F")
        self.assertEqual(Person.objects.filter(sex=OPTION_SEX_MALE).first().sex, "M")
        self.assertEqual(Person.objects.filter(sex=OPTION_SEX_FEMALE).first().get_sex_display(), "FEMALE")
        self.assertEqual(Person.objects.filter(sex=OPTION_SEX_MALE).first().get_sex_display(), "MALE")

        self.assertEqual(Person.objects.filter(name__in=["Sophie", "Claire", "Jim"]).count(), 3)

    def test_comparison_predicates(self):
        self.assertEqual(Person.objects.filter(height__gt=1.75).count(), 4)
        self.assertEqual(Person.objects.filter(height__gte=1.75).count(), 5)
        self.assertEqual(Person.objects.filter(height__lte=1.75).count(), 6)
        self.assertEqual(Person.objects.filter(height__lt=1.75).count(), 5)
        self.assertEqual(Person.objects.filter(height__range=(1.75, 2.00)).count(), 5)

    def test_exclude_predicate(self):
        self.assertEqual(Person.objects.filter(sex=OPTION_SEX_FEMALE).exclude(name="Sophie").count(), 4)

    def test_chaining_predicates(self):
        # Chaining
        self.assertEqual(Person.objects.filter(sex=OPTION_SEX_FEMALE).filter(name="Sophie").count(), 1)

    def test_complex_queries_predicates(self):
        # Q allows building up
        self.assertEqual(Person.objects.filter(Q(name="Sophie") | Q(name="Emma")).count(), 2)
        self.assertEqual(Person.objects.filter(Q(sex=OPTION_SEX_FEMALE), Q(name="Sophie") | Q(name="Emma")).count(), 2)

    def test_referencing_other_fields(self):
        # F allows referencing other fields
        self.assertEqual(Person.objects.filter(name__contains=F("sex")).count(), 2)

    def test_exists_predicates(self):
        self.assertFalse(Person.objects.filter(name="Jimmy").exists())
