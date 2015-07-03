from django.core.urlresolvers import reverse
from django.forms import DecimalField
from django.test import TestCase

from formsintroduction.forms.bastic_form_example import BasicFormExample
from formsintroduction.forms.class_form_example import ClassBasedForm
from viewsintroduction.models import PhoneAddress


class TestBasicForm(TestCase):
    def test_fields(self):
        form = BasicFormExample({})

        self.assertEqual(2, len(form.fields))
        self.assertTrue("height" in form.fields.keys())
        self.assertTrue("name" in form.fields.keys())
        self.assertIsInstance(form.fields['height'], DecimalField)
        self.assertEqual(2, form.fields['height'].max_value)

    def test_valid_data(self):
        form = BasicFormExample({"name": "Luke", "height": 1.11})

        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = BasicFormExample({"name": "Luke"})

        self.assertFalse(form.is_valid())
        self.assertTrue("name" not in form.errors.keys())
        self.assertTrue("height" in form.errors.keys())

        self.assertEqual(form.errors["height"], ['This field is required.'])


class TestClassBasedForm(TestCase):
    def test_valid_data(self):
        form = ClassBasedForm({"number": 123, "street_name": "The high street", "city": "Bristol"})

        self.assertTrue(form.is_valid())

        a_record = form.save()

        self.assertEqual(123, a_record.number)
        self.assertEqual("The high street", a_record.street_name)
        self.assertEqual("Bristol", a_record.city)

    def test_invalid_data(self):
        form = ClassBasedForm({})

        self.assertEqual(form.errors["number"],
                         ['We need a number of the house!', 'None of the fields have been set!!!'])

    def test_meta(self):
        self.assertEqual(PhoneAddress, ClassBasedForm.Meta.model)
        self.assertEqual(("city", "street_name", "number"), ClassBasedForm.Meta.fields)

    def test_post_invalid(self):
        response = self.client.post(reverse("formsintroduction:form_class_create"),
                                    {"city": "Word_Word", "street_name": "street", "number": 1},
                                    follow=True)

        self.assertEqual(200, response.status_code)
        self.assertFormError(response, 'form', 'city', ["Name must be a capitalised single word"])

    def test_post_valid(self):
        response = self.client.post(reverse("formsintroduction:form_class_create"),
                                    {"city": "Foo", "street_name": "Foo", "number": 1},
                                    follow=True)

        self.assertEqual(200, response.status_code)
        self.assertRedirects(response, "http://testserver/viewsintroduction/address/1/", 302)
