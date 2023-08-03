# tests/test_views.py

from django.test import TestCase, Client
from django.urls import reverse
from assets.models import Company


class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.company = Company.objects.create(name="Test Company", description="Test description")

    def test_company_list_view(self):
        response = self.client.get(reverse('company_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.company.name)

    def test_add_company_view(self):
        response = self.client.post(reverse('add_company'), {'name': 'New Company', 'description': 'New description'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        self.assertTrue(Company.objects.filter(name='New Company').exists())
