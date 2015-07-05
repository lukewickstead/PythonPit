from unittest import TestCase

from ...populations.populte_proxy_child import populate
from ...models import ProxyChild, ProxyParent


class TestCreateProxyChild(TestCase):
    """
    Examples of how to create proxy children
    """

    def setUp(self):
        populate()

    def test_create_proxy_children(self):
        self.assertEqual(ProxyChild.objects.all().count(), 3)
        self.assertEqual(ProxyParent.objects.all().count(), 3)
