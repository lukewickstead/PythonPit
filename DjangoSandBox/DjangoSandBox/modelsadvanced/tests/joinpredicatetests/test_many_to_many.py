from unittest import TestCase

from modelsadvanced.populations.populate_author_book import populate
from modelsadvanced.models import Author, Book


class TestManyToMany(TestCase):
    """
    Examples of how to create parents and children who are joined with a n:m (Many to Man) join.

    Both sides can return potentially multiple records; both sides respond to most of the same functionality as found
    within the one to many joins (test_one_to_many.py)
    """

    def setUp(self):
        populate()

    def test_create_author_book(self):
        self.assertEqual(Author.objects.all().count(), 3)
        self.assertEqual(Book.objects.all().count(), 3)

    def test_parent_to_children(self):
        # Each child responds to the field name associated with the join, this returns a manager for parent table;
        # this can then be predicated against the joined parent records
        self.assertEqual(Book.objects.get(name="1984").authors.count(), 3)
        self.assertEqual(Book.objects.get(name="1984").authors.filter(name__contains="o").count(), 3)

    def test_children_to_parent(self):
        # Each parent has a field called <child>_set which returns a manager for child table;
        # this can then be predicated against the joined children records
        self.assertEqual(Author.objects.get(name__contains="George").book_set.count(), 3)
        self.assertEqual(Author.objects.get(name__contains="George").book_set.filter(name__contains="b").count(), 2)
