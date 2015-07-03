from django.core.urlresolvers import reverse, resolve
from django.test import TestCase

from home import views


class TestHomeUrls(TestCase):
    urls = 'home.urls'

    def test_reverse(self):
        self.assertEqual('/', reverse('home'))

    def test_resolve(self):
        resolver = resolve(reverse('home'))

        self.assertEqual(views.home, resolver.func)
        self.assertEqual('home', resolver.url_name)

        self.assertEqual((), resolver.args)
        self.assertEqual({}, resolver.kwargs)
        self.assertEqual(None, resolver.app_name)
        self.assertEqual('', resolver.namespace)


class TestHelloworldUrls(TestCase):
    urls = 'helloworld.urls'

    def test_reverse(self):
        self.assertEqual('/', reverse('default'))
        self.assertEqual('/index/', reverse('index'))
        self.assertEqual('/hello/', reverse('hello'))
        self.assertEqual('/template/', reverse('template'))
        self.assertEqual('/model/', reverse('model'))
        self.assertEqual('/template_loader/', reverse('loader'))
        self.assertEqual('/errors/post_or_get/', reverse('error_if_not_get_or_post'))
        self.assertEqual('/errors/404/', reverse('error_as_404'))
        self.assertEqual('/errors/custom_404/', reverse('error_as_custom_404'))
        self.assertEqual('/errors/not_allowed/', reverse('not_allowed'))
        self.assertEqual('/errors/only_get/', reverse('error_if_not_get'))
        self.assertEqual('/errors/only_post/', reverse('error_if_not_post'))


class TestViewsIntroductionUrls(TestCase):
    urls = 'viewsintroduction.urls'

    def test_reverse(self):
        self.assertEqual('/address/1/update/', reverse('address_update', kwargs={'pk': 1}))
