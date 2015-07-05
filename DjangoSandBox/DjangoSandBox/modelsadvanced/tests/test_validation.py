from unittest import TestCase
from datetime import date

from django.core.exceptions import ValidationError

from ..models import ContactDetails


class TestCreateAuthorBook(TestCase):
    """
    Examples of how to add validation onto models
    """

    def test_create_author_book(self):

        try:
            a_contact = ContactDetails(name="Luke", age=101, contactDate=date(year=2015, month=7, day=2))
            a_contact.full_clean()
        except ValidationError as e:

            self.assertEqual({'name': ['Ensure this value has at least 10 characters (it has 4).', 'Luke is barred'],
                              'age': ['Ensure this value is less than or equal to 100.'],
                              'contactDate': ['2015-07-02 is not a future date.']}, e.message_dict)
