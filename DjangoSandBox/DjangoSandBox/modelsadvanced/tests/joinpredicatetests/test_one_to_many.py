from unittest import TestCase

from django.db.models import Count

from modelsadvanced.populations.populate_parent_and_child import populate
from modelsadvanced.models import Child, Parent


class TestOneToMany(TestCase):
    """
    Examples of how to traverse one to many joins and predicate them
    """

    def setUp(self):
        populate()

    def test_create_parent_and_child(self):
        self.assertEqual(Child.objects.all().count(), 10)
        self.assertEqual(Parent.objects.all().count(), 5)

    def test_parent_to_child(self):
        # Where the child predicates matches more than one child we get duplicates in the QuerySet.
        self.assertEqual(Parent.objects.get(name="Angus").child_set.count(), 2)
        self.assertEqual(Parent.objects.get(name="Angus").child_set.order_by("name").first().name, "Bob")

        # We can search by the actual joined record
        self.assertEqual(Parent.objects.get(child=Child.objects.get(name="Sophie")).name, "Bob")

    def test_child_to_parent(self):
        self.assertEqual(Child.objects.get(name="Sophie").parent.name, "Bob")

        # We can search against parent fields
        self.assertEqual(Child.objects.get(parent__name="Bob").name, "Sophie")

        # We can search by the actual joined record
        self.assertEqual(Child.objects.get(parent=Parent.objects.get(name="Bob")).name, "Sophie")

    def test_predicate_child_set(self):
        # We can query child fields from the parent
        self.assertEqual(Parent.objects.filter(child__name="Sport").count(), 1)
        self.assertEqual(Parent.objects.filter(child__name__contains="S").count(), 3)

        # Where a join is not met Django fills the entities with null
        self.assertEqual(Parent.objects.filter(child__name__isnull=False).count(), 10)
        self.assertEqual(Parent.objects.filter(child__name__isnull=True).count(), 1)

        self.assertEqual(Parent.objects.filter(child__name__contains="S", child__name__icontains="e").count(), 1)
        self.assertEqual(Parent.objects.filter(child__name__contains="S").filter(child__name__contains="p").count(), 3)

        # child_set returns a manager which we can predicate
        self.assertEqual(Parent.objects.get(name="Dave").child_set.filter(name__contains="S").count(), 2)

    def test_prefetch(self):
        # Pre-Populates the join objects so we don't have to hit the database again
        self.assertEqual(Parent.objects.select_related().get(name="Dave").child_set.count(), 5)
        self.assertEqual(Child.objects.select_related().get(name="Sophie").parent.name, "Bob")

    def test_annotate(self):
        parents_with_name = Parent.objects.annotate(children_count=Count("child"))
        self.assertEqual(parents_with_name.get(name="Luke").children_count, 2)
        self.assertEqual(parents_with_name.get(name="Dave").children_count, 5)
