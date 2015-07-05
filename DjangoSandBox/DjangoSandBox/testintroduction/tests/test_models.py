from datetime import date

from django.core.exceptions import ValidationError
from django.test import TestCase

from helloworld.models import HelloWorld
from modelsadvanced.models import ContactDetails, ProxyChild


class TestHelloWorld(TestCase):
    def setUp(self):
        self.first_name = "Luke"
        self.now = date.today()

        self.a_helloworld = HelloWorld(first_name=self.first_name, now=self.now)

    def test_str(self):
        self.assertEqual("{0} {1}".format(self.first_name, self.now), str(self.a_helloworld))

    def test_get_absolute_url(self):
        self.assertEqual("/helloworld/model/", self.a_helloworld.get_absolute_url())


class TestModelValidation(TestCase):
    """
    Examples of how to add validation onto models
    """

    def test_model_validation(self):

        try:
            a_contact = ContactDetails(name="Luke", age=101, contactDate=date(year=2015, month=7, day=2))
            a_contact.full_clean()
        except ValidationError as e:

            self.assertEqual({'name': ['Ensure this value has at least 10 characters (it has 4).', 'Luke is barred'],
                              'age': ['Ensure this value is less than or equal to 100.'],
                              'contactDate': ['2015-07-02 is not a future date.']}, e.message_dict)


class TestModelMeta(TestCase):
    def test_model_meta(self):
        self.assertEqual(True, ProxyChild()._meta.proxy)


class TestModelFields(TestCase):
    def test_model_meta(self):
        field_names = list(map((lambda x: x.name), ContactDetails._meta.fields))

        self.assertEqual(4, len(ContactDetails._meta.fields))
        self.assertEqual(['id', 'age', 'name', 'contactDate'], field_names)
