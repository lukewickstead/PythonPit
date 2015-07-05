from unittest import TestCase

from ...populations.populate_author_book import populate
from ...models import Author, Book


class TestCreateAuthorBook(TestCase):
    """
    Examples of how to create parents and children who are joined with a n:m (Many to Man) join.
    """

    def setUp(self):
        populate()

    def test_create_author_book(self):
        self.assertEqual(Author.objects.all().count(), 3)
        self.assertEqual(Book.objects.all().count(), 3)
