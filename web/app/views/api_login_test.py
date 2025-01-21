from base64 import b64encode

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class APILoginTest(APITestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "testpassword"
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
        )
        self.login_url = reverse("knox_login")

    def test_login_success(self):
        data = {}
        response = self.client.post(
            self.login_url,
            data,
            HTTP_AUTHORIZATION=f"Basic {b64encode(b'testuser:testpassword').decode('utf-8')}",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)

    def test_login_failure(self):
        data = {}
        response = self.client.post(
            self.login_url,
            data,
            HTTP_AUTHORIZATION=f"Basic {b64encode(b'testuser:wrongpassword').decode('utf-8')}",
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn("token", response.data)
