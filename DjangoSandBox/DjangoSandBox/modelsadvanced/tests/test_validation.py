from unittest import TestCase
from datetime import date
from django.core.exceptions import ValidationError
from modelsadvanced.models import ContactDetails


class TestCreateAuthorBook(TestCase):
    """
    Examples of how to add validation onto models
    """

    def test_create_author_book(self):

        try:
            a_contact = ContactDetails(name="Luke", age=101, contactDate=date.today())
            a_contact.full_clean()
        except ValidationError as e:

            self.assertEqual({'name': ['Ensure this value has at least 10 characters (it has 4).', 'Luke is barred'],
                              'contactDate': ['2015-06-29 is not a future date.'],
                              'age': ['Ensure this value is less than or equal to 100.']}, e.message_dict)
