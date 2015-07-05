from unittest import TestCase

from ...populations.populate_abstract_base_child import populate
from ...models import AbstractBaseChild


class TestCreateAbstractBaseChild(TestCase):
    """
    Examples of how to create children of abstract base parents
    """

    def setUp(self):
        populate()

    def test_create_abstract_base_child(self):
        self.assertEqual(AbstractBaseChild.objects.all().count(), 3)
