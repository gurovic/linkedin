from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient


class ApiAuthCheckTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user_client = APIClient()
        self.user_client.force_authenticate(user=self.user)

        self.response_unauth = self.client.get(reverse('api_auth_check'))
        self.response_auth = self.user_client.get(reverse('api_auth_check'))

    def test_status_code(self):
        self.assertEqual(self.response_unauth.status_code, 401)
        self.assertEqual(self.response_auth.status_code, 200)

    def test_content(self):
        response_unauth_json = self.response_unauth.json()
        response_auth_json = self.response_auth.json()
        self.assertTrue("error" in response_unauth_json and response_unauth_json["error"] == "Unauthorized!")
        self.assertTrue("user" in response_auth_json and response_auth_json["user"] == "testuser")
