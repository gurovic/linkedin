from django.test import TestCase
from django.contrib.auth.models import User
from . import Company, Vacancy
from app.models.language import Language
from app.models.major import Major


class CompanyTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.company_data = {
            'name': "Test Company",
            'description': "A company for testing.",
            'country': 'FR'
        }
        self.company = Company.objects.create(**self.company_data)

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
        self.major = Major(name="CS")
        self.language = Language(name="English")
        self.vacancy = Vacancy(
            name="Test Vacancy",
            description="A vacancy for testing.",
            company=self.company,
            expiration_date="2025-01-01",
            contacts="+79123456789",
        )
        self.language.save()
        self.major.save()
        self.company.save()
        self.vacancy.save()
        self.vacancy.required_majors.add(self.major)
        self.vacancy.required_language.add(self.language)

    def test_vacancy_fields(self):
        self.assertEqual(self.vacancy.name, "Test Vacancy")
        self.assertEqual(self.vacancy.description, "A vacancy for testing.")
        self.assertIn(self.major, self.vacancy.required_majors.all())
        self.assertEqual(self.vacancy.expiration_date, "2025-01-01")
        self.assertIn(self.language, self.vacancy.required_language.all())
        self.assertEqual(self.vacancy.contacts, "+79123456789")

    def test_vacancy_company_link(self):
        self.assertEqual(self.vacancy.company, self.company)

        company2 = Company.objects.create(
            name="Another Company",
            description="Second company for testing.",
            country='GB'
        )
        vacancy2 = Vacancy.objects.create(
            name="Test Vacancy 2",
            description="A vacancy for testing.",
            company=company2,
            expiration_date="2025-01-01",
            contacts="+79123456789",
        )
        self.assertEqual(self.vacancy.company, self.company)
        self.assertEqual(vacancy2.company, company2)
