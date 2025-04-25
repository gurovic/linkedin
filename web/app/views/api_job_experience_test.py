from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from ..models import JobExperience

class JobExperienceAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

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

        self.client = APIClient()
        self.url = reverse('job_experience')

    def test_get_all_job_experiences(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0]['company_name'], 'Company A')
        self.assertEqual(response.data[0]['position'], 'Developer')
        self.assertEqual(response.data[0]['start_year'], 2018)
        self.assertEqual(response.data[0]['end_year'], 2020)
        self.assertIn('id', response.data[0])

    def test_get_single_job_experience(self):
        url = f"{self.url}{self.experience1.id}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['company_name'], 'Company A')

    def test_unauthorized_access(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_job_experience_ordering(self):
        response = self.client.get(self.url)
        self.assertLess(
            response.data[0]['start_year'],
            response.data[1]['start_year']
        )