from django.test import TestCase
from django.contrib.auth.models import User
from . import AlumniVerificationRequest

class AlumniVerificationRequestTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_create_request(self):
        request = AlumniVerificationRequest.objects.create(
            user=self.user,
            name='Test AlumniVerificationRequest',
            photo='alumni_verification_request_test/kitten.jpg'
        )
        self.assertEqual(request.name, 'Test AlumniVerificationRequest')
        self.assertEqual(request.user, self.user)
        self.assertIsNotNone(request.date)

    def test_string_representation(self):
        request = AlumniVerificationRequest.objects.create(
            user=self.user,
            name='Test AlumniVerificationRequest',
            photo='alumni_verification_request_test/kitten.jpg'
        )
        expected_str = f'{request.name}, {request.date}'
        self.assertEqual(str(request), expected_str)

    def test_request_user_relationship(self):
        another_user = User.objects.create_user(username='anotheruser', password='anotherpass')
        request = AlumniVerificationRequest.objects.create(
            user=self.user,
            name='Another Test AlumniVerificationRequest',
            photo='alumni_verification_request_test/kitten.jpg'
        )
        self.assertEqual(request.user.username, 'testuser')
        self.assertNotEqual(request.user.username, another_user.username)

