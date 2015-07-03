from django.core.urlresolvers import reverse

from django.test import TestCase

from home import views as home_views
from helloworld import views as helloworld_views
from viewsintroduction.views import PhoneAddressListView
from viewsintroduction.models import PhoneAddress

# References
# https://docs.djangoproject.com/en/1.8/topics/testing/tools
# http://www.mattsnider.com/testing-and-django # fixtures?


class TestFunctionView(TestCase):
    def test_function_view(self):
        response = self.client.get(reverse("home:home"))

        self.assertEqual(200, response.status_code)
        self.assertEqual(home_views.home, response.resolver_match.func)
        self.assertTemplateUsed(response, template_name='home/home.html')

        self.assertContains(response, '<a href="/helloworld/index/">Hello World</a>')
        self.assertContains(response, '<a href="/templatesintroduction/index">Templates</a>')
        self.assertContains(response, '<a href="/formsintroduction/basic/">Forms</a>')
        self.assertContains(response, '<a href="/viewsintroduction/contact/list">Views</a>')


class TestContextData(TestCase):
    def test_context_data(self):
        response = self.client.get(reverse("helloworld:template"))

        self.assertEqual(200, response.status_code)
        self.assertEqual(helloworld_views.with_template, response.resolver_match.func)
        self.assertTemplateUsed(response, template_name='helloworld/template_example.html')

        self.assertEqual('Obelix', response.context["who"])
        self.assertEqual(False, response.context["islong"])

        self.assertContains(response, 'Hello there Obelix!!!')
        self.assertContains(response, 'This was taken with a shortcut!!')


class TestClassView(TestCase):
    def test_with_no_records(self):
        response = self.client.get(reverse("viewsintroduction:address_list"))

        self.assertEqual(200, response.status_code)
        self.assertEqual(PhoneAddressListView.as_view().__name__, response.resolver_match.func.__name__)

        self.assertTemplateUsed(response, template_name='viewsintroduction/base.html')
        self.assertTemplateUsed(response, template_name='viewsintroduction/phoneaddresslist.html')

        self.assertEqual(0, len(response.context["phoneaddress_list"]))
        self.assertContains(response, '<tr><td colspan="6">There are no addresses</td></tr>')

    def test_with_one_record(self):
        an_address = PhoneAddress(number=1, street_name="A", city="A City")
        an_address.save()

        response = self.client.get(reverse("viewsintroduction:address_list"))

        self.assertEqual(200, response.status_code)
        self.assertEqual(PhoneAddressListView.as_view().__name__, response.resolver_match.func.__name__)

        self.assertTemplateUsed(response, template_name='viewsintroduction/base.html')
        self.assertTemplateUsed(response, template_name='viewsintroduction/phoneaddresslist.html')

        context_addresses = response.context['phoneaddress_list']
        expected_addresses = [repr(r) for r in PhoneAddress.objects.all()]

        self.assertEqual(1, len(context_addresses))
        self.assertEqual(an_address, context_addresses.first())

        self.assertQuerysetEqual(context_addresses, expected_addresses, ordered=False)

        self.assertContains(response, an_address.city)
        self.assertContains(response, an_address.number)
        self.assertContains(response, an_address.street_name)

        self.assertNotContains(response, '<tr><td colspan="6">There are no addresses</td></tr>')


class Test404Error(TestCase):
    def test_404_error_is_raised(self):
        response = self.client.get(reverse("helloworld:error_as_404"))
        self.assertEqual(404, response.status_code)


class TestNotAllowed(TestCase):
    def test_not_allowed(self):
        response = self.client.get(reverse("helloworld:not_allowed"))

        self.assertEqual(405, response.status_code)


class TestOnlyPost(TestCase):
    def test_raises_error_on_get(self):
        response = self.client.get(reverse("helloworld:error_if_not_post"))

        self.assertEqual(405, response.status_code)

    def test_all_ok_on_post(self):
        response = self.client.post(reverse("helloworld:error_if_not_post"), {'name': 'Jim'})

        self.assertEqual(200, response.status_code)
        self.assertContains(response, "{0}, this can only be called with a post".format("Jim"))


class TestRedirect(TestCase):
    def test_redirect(self):
        response = self.client.post(reverse("viewsintroduction:redirect_view"))

        self.assertTrue(301, response.status_code)
        self.assertRedirects(response, "http://djangoproject.com", 301, 200)  # Status codes Us/Them
