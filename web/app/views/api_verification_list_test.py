from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from unittest.mock import Mock
from unittest import mock
from django.contrib.auth.models import User
from django.test import Client

from ..serializers.verification_serializer import VerificationRequestSerializer
from ..views.api_verification_list import VerificationRequestView
from ..models import AlumniVerificationRequest

from unittest.mock import patch



class VerificationRequestViewTests(APITestCase):


    def setUp(self):
        self.api = VerificationRequestView()
        self.client = Client()
        self.url = reverse("verification_requests")
        self.user = User.objects.create()

        self.mock_request = Mock(spec=AlumniVerificationRequest)
        self.mock_request.approved = "NA"

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
            date="2025-03-03",
            photo=None,
            approved="DE"
        )

    def test_get_only_not_answered_requests(self):
        response = self.api.get(None)
        for verification in response.data:
            self.assertEqual(verification["approved"], self.mock_request.approved)