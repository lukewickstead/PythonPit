from django.forms import EmailField, CharField
from django.test import TestCase

from viewsintroduction.models import PhoneAddress


# A few assertions which have not been explored in the other tests
# Reference:
# https://docs.djangoproject.com/en/1.8/topics/testing/tools/#assertions


class TestAdditionalAssertions(TestCase):
    def test_assertFieldOutput(self):
        self.assertFieldOutput(EmailField, {'a@a.com': 'a@a.com'}, {'aaa': ['Enter a valid email address.']})

        self.assertFieldOutput(CharField, {'aa': 'aa'},
                               {'word': ['Ensure this value has at most 3 characters (it has 4).'],
                                'a': ['Ensure this value has at least 2 characters (it has 1).']}, [],
                               {"max_length": 3, "min_length": 2})

    def test_assert_num_queries(self):
        with self.assertNumQueries(1):
            PhoneAddress.objects.create(city="Foo", street_name="Foo", number=1)

        self.assertNumQueries(1, lambda: PhoneAddress.objects.create(city="Foo", street_name="Foo", number=1))
