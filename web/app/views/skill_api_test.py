from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Skill


class TestSkillAPI(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.skill1 = Skill.objects.create(name="Python")
        self.skill2 = Skill.objects.create(name="Django")

        self.get_url = reverse("skill-detail", args=[self.skill1.id])
        self.post_url = reverse("skill-list")

    def test_get_skill_authenticated(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.get_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.skill1.name)

    def test_get_skill_unauthenticated(self):
        response = self.client.get(self.get_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_skill_authenticated(self):
        self.client.force_authenticate(user=self.user)

        new_skill_data = {"name": "JavaScript"}

        response = self.client.post(self.post_url, new_skill_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], new_skill_data['name'])

        self.assertTrue(Skill.objects.filter(name=new_skill_data['name']).exists())

    def test_post_skill_unauthenticated(self):
        new_skill_data = {"name": "JavaScript"}
        response = self.client.post(self.post_url, new_skill_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_skill_invalid_data(self):
        self.client.force_authenticate(user=self.user)

        invalid_data = {"name": ""}
        response = self.client.post(self.post_url, invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
