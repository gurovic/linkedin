from django.test import TestCase, Client
from django.utils import timezone
from ..models import Event
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime
from django.urls import reverse
from PIL import Image
import io


class EventListViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username = 'testuser', password = 'password')
        self.client = Client()
        image_io = io.BytesIO()
        image = Image.new('RGB', (100, 100), color = (255, 0, 0))
        image.save(image_io, format = 'JPEG')
        image_io.seek(0)
        self.event1 = Event.objects.create(
            name = "Future Event",
            description = "This is a future event.",
            picture = SimpleUploadedFile(name = 'test_image.jpg', content = image_io.read(), content_type = 'image/jpeg'),
            date = timezone.now() + datetime.timedelta(days = 5),
            location = "Location 1"
        )

    def test_event_list_view_status_code(self):
        response = self.client.get(reverse("event_list"))
        self.assertEqual(response.status_code, 200)

    def test_event_list_view_context(self):
        response = self.client.get(reverse("event_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('event_list' in response.context)
        self.assertEqual(len(response.context['event_list']), 1)
        self.assertEqual(response.context['event_list'][0].name, "Future Event")

    def test_event_image_formatting(self):
        response = self.client.get(reverse("event_list"))
        self.assertEqual(response.status_code, 200)
        event = Event.objects.get(id = self.event1.id)
        self.assertTrue(event.picture.name.startswith("events/test_image"))