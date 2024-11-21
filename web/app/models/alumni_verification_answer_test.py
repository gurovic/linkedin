from django.contrib.auth.models import User
from django.test import TestCase

from . import AlumniVerificationRequest, AlumniVerificationAnswer


class AlumniVerificationAnswerModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.request = AlumniVerificationRequest.objects.create(user=self.user, name='Test Alumni Verification request',
                                                                photo='alumni_verification_request_test/kitten.jpg')

    def test_create_answer(self):
        answer = AlumniVerificationAnswer.objects.create(
            request_answered=self.request,
            name='Test Answer',
            desc='This is a test description.',
            approved=True
        )
        self.assertEqual(answer.name, 'Test Answer')
        self.assertEqual(answer.desc, 'This is a test description.')
        self.assertEqual(answer.approved, True)
        self.assertIsNotNone(answer.date)

    def test_string_representation(self):
        answer = AlumniVerificationAnswer.objects.create(
            request_answered=self.request,
            name='Test Answer',
            desc='This is a test description.',
            approved=True
        )
        expected_str = f'{answer.name}, {answer.desc}, {answer.approved}, {answer.date}'
        self.assertEqual(str(answer), expected_str)

    def test_answer_request_relationship(self):
        answer = AlumniVerificationAnswer.objects.create(
            request_answered=self.request,
            name='Test Answer',
            desc='This is a test description.',
            approved=True
        )
        request = answer.request_answered
        self.assertEqual(request.name, self.request.name)
        self.assertIsNotNone(request.date)
        self.assertEqual(request.user, self.request.user)
        self.assertEqual(request.photo, self.request.photo)
