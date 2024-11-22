from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models.company import Company


class CompanyListViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.company1 = Company.objects.create(name='Company One', description='A company for testing.', country='CA')
        self.company2 = Company.objects.create(name='Company Two', description='A company for testing.', country='CA')

        self.response = self.client.get(reverse('company_list'))

    def tearDown(self):
        self.company1.delete()
        self.company2.delete()
        self.user.delete()

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'app/company_list.html')

    def test_context(self):
        self.assertIn('companies', self.response.context)
        self.assertEqual(len(self.response.context['companies']), 2)

    def test_contains_companies(self):
        self.assertContains(self.response, 'Company One')
        self.assertContains(self.response, 'Company Two')
