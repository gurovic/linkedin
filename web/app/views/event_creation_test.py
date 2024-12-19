from django.conf import settings
from django.test import Client, TestCase
from django.urls import reverse

from app.forms.event_creation_form import EventForm
from app.models import Event


class EventCreationViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("event_creation")

    def test_event_creation_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/event_creation.html")
        self.assertIsInstance(response.context["form"], EventForm)

    def test_event_creation_post_valid(self):
        data = {
            "name": "Test Event",
            "date": "2023-12-31",
            "location": "Test Location",
            "description": "Test Description",
            "picture": (
                settings.BASE_DIR
                / "app/models/alumni_verification_request_test/kitten.jpg"
            ),
        }
        response = self.client.post(self.url, data)
        self.assertRedirects(response, reverse("event_list"))
        self.assertTrue(Event.objects.filter(name="Test Event").exists())

    def test_event_creation_post_invalid(self):
        data = {
            "name": "",
            "date": "invalid-date",
            "location": "",
            "description": "",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/event_creation.html")
        self.assertFalse(Event.objects.exists())
        form = response.context["form"]
        self.assertFormError(form, "name", "Обязательное поле.")
        self.assertFormError(form, "date", "Введите правильную дату и время.")
