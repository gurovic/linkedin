import io
import os
from PIL import Image

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.utils import timezone

from . import Event


class EventModelTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username = 'user1', password = 'password')
        self.user2 = User.objects.create_user(username = 'user2', password = 'password')

        self.event = Event.objects.create(
            name = 'Test Event',
            description = 'This is a test event',
            date = timezone.now(),
            location = 'Test Location'
        )

        self.allowed_event = Event.objects.create(
            name='Test Event',
            description='This is a test event',
            date=timezone.now(),
            location='Test Location',
            allowed=True
        )

        self.not_allowed_event = Event.objects.create(
            name='Test Event',
            description='This is a test event',
            date=timezone.now(),
            location='Test Location',
            allowed=False
        )

        self.past_event = Event.objects.create(
            name = 'Past Event',
            description = 'This event happened in the past',
            date = timezone.now() - timezone.timedelta(days = 2),
            location = 'Test Location'
        )

        img = Image.new('RGB', (100, 100), color = 'red')
        image_io = io.BytesIO()
        img.save(image_io, format = 'JPEG')

        self.event_with_image = Event.objects.create(
            name = "Test Event",
            date = timezone.make_aware(timezone.datetime(2023, 1, 1)),
            picture = SimpleUploadedFile('test_image.jpg', image_io.getvalue(), content_type='image/jpeg')
        )
        self.event_without_image = Event.objects.create(
            name = "Event without image",
            date = timezone.make_aware(timezone.datetime(2023, 2, 1))
        )

    def tearDown(self):
        if self.event_with_image.picture:
            picture_path = self.event_with_image.picture.path
            self.event_with_image.picture.close()
            if os.path.exists(picture_path):
                os.remove(picture_path)
            self.event_with_image.picture.delete(save = False)
        Event.objects.all().delete()

    def test_event_creation(self):
        self.assertEqual(self.event.name, 'Test Event')
        self.assertEqual(self.event.description, 'This is a test event')
        self.assertAlmostEqual(self.event.date, timezone.now(), delta = timezone.timedelta(seconds = 1))
        self.assertEqual(self.event.location, 'Test Location')

    def test_str_method(self):
        self.assertEqual(str(self.event), 'Test Event')

    def test_many_to_many_field(self):
        self.event.participants.add(self.user1, self.user2)
        self.event.participants.remove(self.user1)
        self.assertNotIn(self.user1, self.event.participants.all())
        self.assertIn(self.user2, self.event.participants.all())


    def test_event_modify(self):
        self.event.name = 'Updated Event Name'
        self.event.save()
        updated_event = Event.objects.get(id = self.event.id)
        self.assertEqual(updated_event.name, 'Updated Event Name')

    def test_already_passed(self):
        self.assertTrue(self.past_event.already_passed())
        self.assertFalse(self.event.already_passed())

    def test_allowed_event(self):
        self.assertTrue(self.allowed_event.allowed)
        self.assertFalse(self.not_allowed_event.allowed)

    def test_format_image_to_height(self):
        target_height = 50
        self.event_with_image.format_image_to_height(target_height)
        img = Image.open(self.event_with_image.picture)
        self.assertEqual(img.height, target_height)
        expected_width = int(target_height * (100 / 100))
        self.assertEqual(img.width, expected_width)
        img.close()

    def test_format_image_to_height_no_image(self):
        with self.assertRaises(ValueError):
            self.event_without_image.format_image_to_height(50)