from django.test import TestCase, Client
from django.urls import reverse

class RoutesTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home(self):
        r = self.client.get(reverse('home'))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Página inicial')

    def test_sobre(self):
        r = self.client.get(reverse('sobre'))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Sobre o site')

    def test_contato(self):
        r = self.client.get(reverse('contato'))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Contato')
