from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from ..models import JobExperience
from rest_framework.authtoken.models import Token


class JobExperienceAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

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
        self.assertEqual(len(response.data['results']), 2)  # Используем ['results'] если включена пагинация

        first_exp = response.data['results'][0] if 'results' in response.data else response.data[0]
        self.assertEqual(first_exp['company_name'], 'Company A')
        self.assertEqual(first_exp['position'], 'Developer')
        self.assertEqual(first_exp['start_year'], 2018)
        self.assertEqual(first_exp['end_year'], 2020)
        self.assertIn('id', first_exp)

    def test_get_single_job_experience(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['company_name'], 'Company A')
        self.assertEqual(response.data['id'], self.experience1.id)

    def test_job_experience_ordering(self):
        response = self.client.get(self.url)
        data = response.data['results'] if 'results' in response.data else response.data

        self.assertLessEqual(
            data[0]['start_year'],
            data[1]['start_year']
        )

    def test_unauthorized_access(self):
        self.client.credentials()
        response = self.client.get(self.url)
        self.assertIn(response.status_code, [401, 403])