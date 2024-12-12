from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class ChangePasswordViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='old_password')
        self.client.login(username='testuser', password='old_password')  # Log the user in

    def test_change_password_success(self):
        response = self.client.post(reverse('change_password'), {
            'current_password': 'old_password',
            'new_password': 'new_password123',
            'confirm_new_password': 'new_password123',
        })

        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('new_password123'))
        self.assertRedirects(response, reverse('home'))

    def test_change_password_incorrect_current_password(self):
        response = self.client.post(reverse('change_password'), {
            'current_password': 'wrong_password',
            'new_password': 'new_password123',
            'confirm_new_password': 'new_password123',
        })

        self.user.refresh_from_db()
        self.assertFalse(self.user.check_password('new_password123'))
        self.assertContains(response, "The current password is incorrect.", html=True)

    def test_change_password_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('change_password'))
        self.assertNotEqual(response.status_code, 404)
