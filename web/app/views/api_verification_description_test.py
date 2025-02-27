from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from django.http.response import Http404

from ..serializers.verification_serializer import VerificationRequestSerializer
from ..views.api_verification_description import VerificationDescriptionView
from ..models import AlumniVerificationRequest


class VerificationRequestViewTests(APITestCase):
    def setUp(self):
        self.api = VerificationDescriptionView()
        self.user = User.objects.create_user(username="andrew")

        self.request1 = AlumniVerificationRequest.objects.create(
            user=self.user,
            date="2025-03-03",
            photo=None,
            approved="NA"
        )

        self.request2 = AlumniVerificationRequest.objects.create(
            user=self.user,
            date="2025-03-03",
            photo=None,
            approved="AC"
        )

        self.request3 = AlumniVerificationRequest.objects.create(
            user=self.user,
            date="2025-03-05",
            photo=None,
            approved="DE"
        )

    def test_responses(self):
        with self.assertRaises(Http404):
            self.api.get(None, 536)
        response1 = self.api.get(None, 1)
        response2 = self.api.get(None, 2)
        response3 = self.api.get(None, 3)
        self.assertEqual(response1.data, VerificationRequestSerializer(self.request1).data)
        self.assertEqual(response2.data, VerificationRequestSerializer(self.request2).data)
        self.assertEqual(response3.data, VerificationRequestSerializer(self.request3).data)
