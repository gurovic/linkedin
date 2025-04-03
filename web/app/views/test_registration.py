from django.test import TestCase, override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from app.forms.registration_form import RegistrationForm


@override_settings(AUTH_PASSWORD_VALIDATORS=[])  # ✅ отключаем валидаторы на время тестов
class SignUpViewTests(TestCase):

    def test_registration_view_get(self):
        response = self.client.get(reverse('registration'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/register.html')
        self.assertIsInstance(response.context['form'], RegistrationForm)

    def test_registration_view_post_valid_data(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'password123',
            'password2': 'password123',
        }
        response = self.client.post(reverse('registration'), data)
        self.assertRedirects(response, reverse('home'))

        user = get_user_model().objects.get(username='testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('password123'))

    def test_registration_view_post_invalid_data(self):
        data = {
            'username': 'testuser',
            'email': 'invalid-email',
            'password1': 'password123',
            'password2': 'differentpassword',
        }
        response = self.client.post(reverse('registration'), data)

        form = response.context['form']  # <- берём user_form явно

        self.assertEqual(response.status_code, 200)
        self.assertIn('email', form.errors)
        self.assertIn('Enter a valid email address.', form.errors['email'])
        self.assertIn('password2', form.errors)
        self.assertIn('The two password fields didn’t match.', form.errors['password2'])
    def test_registration_view_csrf_exempt(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'password123',
            'password2': 'password123',
        }
        response = self.client.post(reverse('registration'), data, HTTP_X_CSRFTOKEN="fake-token")
        self.assertEqual(response.status_code, 302)

    def test_user_is_logged_in_after_registration(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'password123',
            'password2': 'password123',
        }
        response = self.client.post(reverse('registration'), data)
        self.assertTrue(response.wsgi_request.user.is_authenticated)