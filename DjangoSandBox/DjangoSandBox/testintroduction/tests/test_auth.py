from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase


class TestAuthedView(TestCase):
    def test_redirect_to_loging(self):
        response = self.client.post(reverse("auth:users"))

        self.assertTrue(302, response.status_code)
        self.assertRedirects(response, "auth/login/?next=/auth/users/", 302, 200)

    def test_can_login(self):
        user = User.objects.create_user(username='FOOTESTFOO', password='pwd')
        user.is_active = True
        user.save()

        login = self.client.login(username='FOOTESTFOO', password='pwd')

        self.assertTrue(login)

        response = self.client.post(reverse("auth:users"))

        self.assertTrue(200, response.status_code)
        self.assertContains(response, "Registered Users")
        self.assertContains(response, "First Name")
        self.assertContains(response, "Last Name")
        self.assertContains(response, "FOOTESTFOO")
