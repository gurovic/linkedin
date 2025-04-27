from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from ..models import JobExperience
from rest_framework import status


class JobExperienceAPITests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            password='testpass123'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            password='testpass123'
        )

        self.client = APIClient()

        JobExperience.objects.create(
            user=self.user1,
            company_name='Company A',
            start_year=2020,
            end_year=2022,
            position='Developer'
        )
        JobExperience.objects.create(
            user=self.user1,
            company_name='Company B',
            start_year=2022,
            end_year=2023,
            position='Senior Developer'
        )
        JobExperience.objects.create(
            user=self.user2,
            company_name='Other Company',
            start_year=2019,
            end_year=2021,
            position='Manager'
        )

        self.url = reverse('job_experience')

    def test_get_own_experiences_when_authenticated(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        for exp in response.data:
            self.assertEqual(exp['user'], self.user1.id)

    def test_filter_by_user_id(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(f"{self.url}?user_id={self.user2.id}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user'], self.user2.id)
        self.assertEqual(response.data[0]['company_name'], 'Other Company')

    def test_get_own_experiences_when_no_user_id_provided(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        for exp in response.data:
            self.assertEqual(exp['user'], self.user1.id)

    def test_unauthorized_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cannot_access_other_user_without_filter(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(self.url)
        user_ids = {exp['user'] for exp in response.data}
        self.assertEqual(user_ids, {self.user1.id})