from unittest import TestCase

from modelsadvanced.populations.populate_parent_and_child import populate
from modelsadvanced.models import Child, Parent


class TestCreateParentAndChild(TestCase):
    """
    Examples of how to create children and parents of 1:n (One to Many) joins
    """

    def setUp(self):
        populate()

    def test_create_parent_and_child(self):
        self.assertEqual(Child.objects.all().count(), 10)
        self.assertEqual(Parent.objects.all().count(), 5)
