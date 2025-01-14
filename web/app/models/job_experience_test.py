from django.test import TestCase
from django.contrib.auth.models import User
from . import JobExperience


class JobExperienceTest(TestCase):
    company_name = "Yandex"
    start_year = 2017
    end_year = 2019
    position = "Junior backend developer"


    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_create_request(self):
        job_experience = JobExperience.objects.create(
            user=self.user,
            company_name=self.company_name,
            start_year=self.start_year,
            end_year=self.end_year,
            position=self.position
        )
        self.assertEqual(job_experience.user, self.user)
        self.assertEqual(job_experience.company_name, self.company_name)
        self.assertEqual(job_experience.start_year, self.start_year)
        self.assertEqual(job_experience.end_year, self.end_year)
        self.assertEqual(job_experience.position, self.position)

    def test_string_representation(self):
        job_experience = JobExperience.objects.create(
            user=self.user,
            company_name=self.company_name,
            start_year=self.start_year,
            end_year=self.end_year,
            position=self.position
        )
        expected_str = f"{self.company_name} ({self.start_year} - {self.end_year})"
        self.assertEqual(str(job_experience), expected_str)

    def test_request_user_relationship(self):
        another_user = User.objects.create_user(username="anotheruser", password="anotherpass")
        job_experience = JobExperience.objects.create(
            user=self.user,
            company_name=self.company_name,
            start_year=self.start_year,
            end_year=self.end_year,
            position=self.position
        )
        self.assertEqual(job_experience.user.username, "testuser")
        self.assertNotEqual(job_experience.user.username, another_user.username)
