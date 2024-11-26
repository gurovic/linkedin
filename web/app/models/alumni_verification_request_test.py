from django.test import TestCase
from django.contrib.auth.models import User
from . import AlumniVerificationRequest


class AlumniVerificationRequestTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_create_request(self):
        alumni_verification_request = AlumniVerificationRequest.objects.create(
            user=self.user,
            photo='alumni_verification_request_test/kitten.jpg'
        )
        self.assertEqual(alumni_verification_request.user, self.user)
        self.assertIsNotNone(alumni_verification_request.date)
        self.assertEqual(alumni_verification_request.approved, 'NA')

    def test_string_representation(self):
        alumni_verification_request = AlumniVerificationRequest.objects.create(
            user=self.user,
            photo='alumni_verification_request_test/kitten.jpg'
        )
        expected_str = f'{alumni_verification_request.user.last_name}, {alumni_verification_request.get_approved_display()}'
        self.assertEqual(str(alumni_verification_request), expected_str)

    def test_request_user_relationship(self):
        another_user = User.objects.create_user(username='anotheruser', password='anotherpass')
        alumni_verification_request = AlumniVerificationRequest.objects.create(
            user=self.user,
            photo='alumni_verification_request_test/kitten.jpg'
        )
        self.assertEqual(alumni_verification_request.user.username, 'testuser')
        self.assertNotEqual(alumni_verification_request.user.username, another_user.username)
