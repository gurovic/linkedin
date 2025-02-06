from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import University, UniversityStudent


class UserDetailViewTests(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass', first_name='Test',
                                             last_name='User')

        # Create a university
        self.university = University.objects.create(name='Test University')

        # Create a UniversityStudent relationship
        UniversityStudent.objects.create(student=self.user, university=self.university, start_year="2024-10-10")

    def test_get_user_detail(self):
        url = reverse('user-detail', args=[self.user.id])  # Adjust the URL name as necessary
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.user.first_name)
        self.assertEqual(response.data['last_name'], self.user.last_name)
        self.assertEqual(len(response.data['university']), 1)
        self.assertEqual(response.data['university'][0]['name'], self.university.name)

    def test_get_user_detail_not_found(self):
        url = reverse('user-detail', args=[999])  # Non-existent user ID
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
