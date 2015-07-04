from unittest import TestCase

from modelsadvanced.populations.populate_multi_table_base_child import populate
from modelsadvanced.models import MultiTableBaseChild, MultiTableBaseParent


class TestCreateMultiTableBasedChild(TestCase):
    """
    Examples of how to create children and parents of multi table based inheritance
    """

    def setUp(self):
        populate()

    def test_create_multi_table_based_Child(self):
        self.assertEqual(MultiTableBaseChild.objects.all().count(), 3)
        self.assertEqual(MultiTableBaseParent.objects.all().count(), 3)
