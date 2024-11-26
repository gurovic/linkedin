from django.test import TestCase
from django.contrib.auth.models import User
from . import Company, Vacancy

class CompanyTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.company_data = {
            'name': "Test Company",
            'description': "A company for testing.",
            'country': 'FR'
        }
        self.company = Company.objects.create(**self.company_data)

    def tearDown(self):
        Company.objects.all().delete()
        User.objects.all().delete()

    def test_create_company(self):
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
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.company = Company.objects.create(
            name="Test Company",
            description="A company for testing.",
            country='FR'
        )
        self.vacancy_data = {
            'name': "Test Vacancy",
            'description': "A vacancy for testing.",
            'needed_majorsubject': 'CS',
            'company': self.company
        }
        self.vacancy = Vacancy.objects.create(**self.vacancy_data)

    def test_vacancy_fields(self):
        self.assertTrue(Vacancy.objects.filter(name="Test Vacancy").exists())
        self.assertEqual(self.vacancy.name, "Test Vacancy")
        self.assertEqual(self.vacancy.description, "A vacancy for testing.")
        self.assertEqual(self.vacancy.needed_majorsubject, "CS")

    def test_vacancy_company_link(self):
        self.assertEqual(self.vacancy.company, self.company)

        company2 = Company.objects.create(
            name="Another Company",
            description="Second company for testing.",
            country='GB'
        )
        vacancy2 = Vacancy.objects.create(
            name="Another Vacancy",
            description="Second vacancy for testing.",
            needed_majorsubject='MATH',
            company=company2
        )
        self.assertEqual(self.vacancy.company, self.company)
        self.assertEqual(vacancy2.company, company2)
