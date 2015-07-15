# Reference:
# Cookies[key] returns a http.cookies.Morsel class; https://docs.python.org/2/library/cookie.html

from django.core.urlresolvers import reverse
from django.test import TestCase


class TestSessions(TestCase):
    def test_cookie(self):
        response = self.client.post(reverse("sessionsandcookies:cookies"))

        self.assertTrue(200, response.status_code)

        self.assertTrue("hits" in self.client.cookies)
        self.assertEqual('1', self.client.cookies["hits"].value)
        self.assertEqual(30, self.client.cookies["hits"]["max-age"])

    def test_sessions(self):
        response = self.client.post(reverse("sessionsandcookies:sessions"))

        self.assertTrue(200, response.status_code)

        self.assertTrue("has_visited" in self.client.session)
        self.assertEqual('True', self.client.session["has_visited"])
        self.assertEqual(10, self.client.session.get_expiry_age())
