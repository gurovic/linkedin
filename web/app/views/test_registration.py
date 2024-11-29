from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms
from app.forms.registration_form import RegistrationForm


class SignUpViewTests(TestCase):

    def test_registration_view_get(self):
        """Test GET request to sign up page returns the correct form."""
        response = self.client.get(reverse('registration'))  # Replace with actual URL name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/register.html')
        self.assertIsInstance(response.context['form'], RegistrationForm)

    def test_registration_view_post_valid_data(self):
        """Test POST request with valid data creates a new user and redirects."""
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'password123',
            'password2': 'password123',
        }
        response = self.client.post(reverse('registration'), data)

        # Check if the user is redirected after a successful sign-up
        self.assertRedirects(response, reverse('home'))

        # Check if the user is created
        user = get_user_model().objects.get(username='testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('password123'))  # Ensure password is hashed

    def test_registration_view_post_invalid_data(self):
        """Test POST request with invalid data shows errors."""
        data = {
            'username': 'testuser',
            'email': 'invalid-email',
            'password1': 'password123',
            'password2': 'differentpassword',
        }
        response = self.client.post(reverse('registration'), data)

        form = response.context['form']
        # Check if the form is returned with errors
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')
        self.assertFormError(response, 'form', 'password2', 'The two password fields didn’t match.')

    def test_registration_view_csrf_exempt(self):
        """Test if CSRF exemption works for the sign-up view."""
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'password123',
            'password2': 'password123',
        }
        response = self.client.post(reverse('registration'), data, HTTP_X_CSRFTOKEN="fake-token")

        # Since we have @csrf_exempt, the CSRF token should not cause a failure
        self.assertEqual(response.status_code, 200)  # Should redirect on success


    def test_user_is_logged_in_after_registration(self):
        """Test that the user is logged in after a successful sign up."""
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'password123',
            'password2': 'password123',
        }
        response = self.client.post(reverse('registration'), data)

        # Check if user is logged in after sign-up
        self.assertTrue(response.wsgi_request.user.is_authenticated)
