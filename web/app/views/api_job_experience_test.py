from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from ..models import JobExperience


class JobExperienceAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.experience1 = JobExperience.objects.create(
            user=self.user,
            company_name='Company A',
            start_year=2018,
            end_year=2020,
            position='Developer'
        )
        self.experience2 = JobExperience.objects.create(
            user=self.user,
            company_name='Company B',
            start_year=2020,
            end_year=2022,
            position='Senior Developer'
        )

        self.url = reverse('job_experience')

    def test_get_all_job_experiences(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

        company_names = {exp['company_name'] for exp in response.data}
        self.assertIn('Company A', company_names)
        self.assertIn('Company B', company_names)

    def test_get_single_job_experience(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_job_experience_ordering(self):
        response = self.client.get(f"{self.url}?ordering=start_year")

        self.assertEqual(response.data[0]['start_year'], 2020)
        self.assertEqual(response.data[1]['start_year'], 2018)

    def test_unauthorized_access(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)