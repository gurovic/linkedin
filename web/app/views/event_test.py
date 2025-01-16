from pathlib import Path

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Event
from web.settings import BASE_DIR


class TestEventView(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass",
        )
        self.client.force_authenticate(user=self.user)
        self.event = Event.objects.create(
            name="Test Event",
            description="Test Description",
            date="2025-01-01",
            location="Test Location",
            picture="",
        )
        self.event2 = Event.objects.create(
            name="Test Event2",
            description="Test Description2",
            date="2025-01-02",
            location="Test Location2",
            picture="",
        )

    def test_get_all_events(self):
        url = reverse("events")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Test Event")
        self.assertContains(response, "Test Event2")

    def test_get_single_event(self):
        url = reverse("event_detail", args=[self.event.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_event(self):
        url = reverse("events")
        with Path(
            BASE_DIR / "app/models"
            "/alumni_verification_request_test/kitten.jpg",
        ).open("rb") as image:
            data = {
                "name": "New Event",
                "description": "New Description",
                "date": "2025-01-01",
                "location": "New Location",
                "picture": SimpleUploadedFile(
                    "kitten.jpg",
                    image.read(),
                    content_type="image/jpeg",
                ),
            }
            response = self.client.post(url, data, format="multipart")
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Event.objects.count(), 3)

    def test_update_event(self):
        url = reverse("event_detail", args=[self.event.id])
        data = {
            "name": "Updated Event",
            "description": "Updated Description",
            "date": "2025-01-02",
            "location": "Updated Location",
            "picture": "",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_event(self):
        url = reverse("event_detail", args=[self.event.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Event.objects.count(), 1)


class TestEventParticipantsView(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass",
        )
        self.user2 = User.objects.create_user(
            username="testuser2",
            password="1",
        )
        self.client.force_authenticate(user=self.user)
        self.event = Event.objects.create(
            name="Test Event",
            description="Test Description",
            date="2025-01-01",
            location="Test Location",
            picture="",
        )
        self.event.participants.add(self.user2)

    def test_get_event_participants(self):
        url = reverse("event_participants", args=[self.event.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "testuser")

    def test_add_event_participant(self):
        url = reverse("event_participants", args=[self.event.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(self.event.participants.contains(self.user))

    def test_remove_event_participant(self):
        self.event.participants.add(self.user)
        url = reverse("event_participants", args=[self.event.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.event.participants.count(), 1)
