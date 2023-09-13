from django.urls import reverse
from django.test import SimpleTestCase


class PagesTest(SimpleTestCase):

    def test_home_page(self):
        self.assertEqual(reverse('home'), '/')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
