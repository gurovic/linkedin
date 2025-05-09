import io
import datetime
from PIL import Image

from django.test import TestCase, Client
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from ..models import Event


class EventListViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = Client()
        image_io = io.BytesIO()
        image = Image.new('RGB', (100, 100), color=(255, 0, 0))
        image.save(image_io, format='JPEG')
        image_io.seek(0)
        self.event1 = Event.objects.create(
            name="Future Event",
            description="This is a future event.",
            picture=SimpleUploadedFile(name='test_image.jpg', content=image_io.read(), content_type='image/jpeg'),
            date=timezone.now() + datetime.timedelta(days=5),
            location="Location 1",
            allowed = True
        )
        self.event2 = Event.objects.create(
            name="Denied Event",
            description="This event is not allowed.",
            picture=SimpleUploadedFile(name='test_image2.jpg', content=image_io.read(), content_type='image/jpeg'),
            date=timezone.now() + datetime.timedelta(days=10),
            location="Location 2",
            allowed=False
        )

    def tearDown(self):
        self.event1.picture.delete(save=False)
        Event.objects.all().delete()

    def test_event_list_view_status_code(self):
        response = self.client.get(reverse("event_list_old"))
        self.assertEqual(response.status_code, 200)

    def test_event_list_view_context(self):
        response = self.client.get(reverse("event_list_old"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('event_list' in response.context)
        self.assertEqual(len(response.context['event_list']), 1)
        self.assertEqual(response.context['event_list'][0].name, "Future Event")

    def test_event_image_formatting(self):
        response = self.client.get(reverse("event_list_old"))
        self.assertEqual(response.status_code, 200)
        event = Event.objects.get(id=self.event1.id)
        self.assertTrue(event.picture.name.startswith("events/test_image"))