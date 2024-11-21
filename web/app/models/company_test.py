from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from company import Company, Vacancy

class CompanyTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.company_data = {
            'name': "Test Company",
            'description': "A company for testing.",
            'country': 'FR'
        }
        self.company = Company.objects.create(**self.company_data)

    def tearDown(self):
        Company.objects.all().delete()
        User.objects.all().delete()


    def test_create_company_page(self):
        response = self.client.get(reverse('company_create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create Company")

    def test_create_company(self):
        response = self.client.post(reverse('company_create'), self.company_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Company.objects.filter(name="Test Company").exists())

    def test_company_str(self):
        self.assertEqual(str(self.company), "Test Company")

    def test_add_worker(self):
        self.company.current_workers.add(self.user)
        self.assertIn(self.user, self.company.current_workers.all())

    def test_remove_worker(self):
        self.company.current_workers.add(self.user)
        self.company.current_workers.remove(self.user)
        self.assertNotIn(self.user, self.company.current_workers.all())

    def test_current_workers(self):
        user2 = User.objects.create_user(username='testuser2', password='testpass2')
        self.company.current_workers.add(self.user)
        self.company.current_workers.add(user2)
        workers = list(self.company.current_workers.all())
        self.assertEqual(len(workers), 2)
        self.assertIn(self.user, workers)
        self.assertIn(user2, workers)


class VacancyTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.company = Company.objects.create(
            name="Test Company",
            description="A company for testing.",
            country='FR'
        )
        self.vacancy_data = {
            'name': "Test Vacancy",
            'description': "A vacancy for testing.",
            'needed_majorsubject': 'CS',
            'company': self.company.id
        }

    def tearDown(self):
        Vacancy.objects.all().delete()
        Company.objects.all().delete()
        User.objects.all().delete()


    def test_create_vacancy_page(self):
        response = self.client.get(reverse('vacancy_create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create Vacancy")

    def test_create_vacancy(self):
        response = self.client.post(reverse('vacancy_create'), self.vacancy_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Vacancy.objects.filter(name="Test Vacancy").exists())

    def test_vacancy_str(self):
        vacancy = Vacancy.objects.create(**self.vacancy_data)
        self.assertEqual(str(vacancy), "Test Vacancy")