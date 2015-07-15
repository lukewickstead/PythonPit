# Reference:
# https://docs.djangoproject.com/en/1.8/topics/db/examples/many_to_many
# https://docs.djangoproject.com/en/1.8/topics/db/examples/many_to_one/
# https://docs.djangoproject.com/en/1.8/topics/db/examples/one_to_one/

from unittest import TestCase

from ...models import Parent, Child, Author, Book


def delete_all(records):
    for a_record in records:
        try:
            a_record.delete()
        except AssertionError:
            print("Issue clearing up")


class TestJoinAssigningOneToMany(TestCase):
    def tearDown(self):
        delete_all(self.to_delete)

    def test_assigning_children(self):
        # OneToOne / ForeignKey responds to all functionality of ManyToMany except remove and clear()

        self.to_delete = list()

        a_parent = Parent(name="Temp")
        a_parent.save()
        self.to_delete.append(a_parent)

        a_child = Child(name="Temp")
        a_child.save()
        self.to_delete.append(a_child)

        a_parent.child_set.add(a_child)
        self.assertIn(a_child, a_parent.child_set.all())

        a_parent.delete()  # Cascade delete by default will delete all associated children
        self.to_delete = list()


class TestJoinAssigningManyToMany(TestCase):
    def tearDown(self):
        delete_all(self.to_delete)

    def test_assigning_children(self):
        self.to_delete = list()

        a_parent = Author(name="Temp")
        a_parent.save()
        self.to_delete.append(a_parent)

        a_child = Book(name="Temp")
        a_child.save()
        self.to_delete.append(a_child)

        a_parent.book_set.add(a_child)
        self.assertIn(a_child, a_parent.book_set.all())
        a_parent.book_set.remove(a_child)

        self.assertEqual(0, a_parent.book_set.all().count())

    def test_assigning_multiple_children(self):
        # Either the <FieldName> or <FieldName>+set will return the collection of associated joins;
        # depending upon if you are on the child or parent

        # Assignment can also be made with the constructor/create/get_or_create etc

        self.to_delete = list()

        a_parent = Author(name="Temp")
        a_parent.save()
        self.to_delete.append(a_parent)

        a_child = Book(name="Temp")
        a_child.save()
        self.to_delete.append(a_child)

        a_child_two = Book(name="TempTwo")
        a_child_two.save()
        self.to_delete.append(a_child_two)

        a_parent.book_set.add(a_child, a_child_two)
        self.assertSequenceEqual([a_child, a_child_two], a_parent.book_set.all())

        a_parent.book_set.clear()
        self.assertEqual(a_parent.book_set.all().count(), 0)

        a_parent.book_set = [a_child, a_child_two]
        self.assertSequenceEqual([a_child, a_child_two], a_parent.book_set.all())


class TestJoinAssigningParent(TestCase):
    """
    Example of how to set parent/child for 1:1 or parent on 1:n
    """

    def tearDown(self):
        delete_all(self.to_delete)

    def test_assigning_parent(self):
        self.to_delete = list()

        a_parent = Parent(name="Temp")
        a_parent.save()
        self.to_delete.append(a_parent)

        a_child = Child(name="Temp")
        a_child.parent = a_parent
        a_child.save()
        self.to_delete.append(a_child)

        self.assertIn(a_child, a_parent.child_set.all())

        a_parent.delete()  # Cascade delete by default will delete all associated children
        self.to_delete = list()
