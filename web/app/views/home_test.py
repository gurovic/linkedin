import datetime
import io
from PIL import Image

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile

from ..models import Event
from ..models.company import Company

class HomeViewTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='password1')
        self.user2 = User.objects.create_user(username='testuser2', password='password2')

        self.company1 = Company.objects.create(
            name='Company One',
            description='Test Company 1',
            country='US'
        )
        self.company2 = Company.objects.create(
            name='Company Two',
            description='Test Company 2',
            country='CA'
        )

        image_io = io.BytesIO()
        image = Image.new('RGB', (300, 300), color=(255, 0, 0))
        image.save(image_io, format='JPEG')
        image_io.seek(0)

        self.future_event = Event.objects.create(
            name="Future Event",
            description="An upcoming event",
            picture=SimpleUploadedFile(
                name='future_event.jpg',
                content=image_io.read(),
                content_type='image/jpeg'
            ),
            date=timezone.now() + datetime.timedelta(days=10),
            location="Future Location"
        )

        self.past_event = Event.objects.create(
            name="Past Event",
            description="An past event",
            picture=None,
            date=timezone.now() - datetime.timedelta(days=10),
            location="Past Location"
        )

        self.response = self.client.get(reverse('home'))

    def tearDown(self):
        if hasattr(self.future_event, 'picture') and self.future_event.picture:
            self.future_event.picture.delete(save=False)

    def test_home_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_view_template(self):
        self.assertTemplateUsed(self.response, 'app/home.html')

    def test_home_view_context(self):
        self.assertIn('users', self.response.context)
        self.assertIn('event_list', self.response.context)
        self.assertIn('companies', self.response.context)

    def test_users_in_context(self):
        users = self.response.context['users']
        self.assertEqual(users.count(), 2)
        self.assertTrue(self.user1 in users)
        self.assertTrue(self.user2 in users)

    def test_events_in_context(self):
        events = self.response.context['event_list']
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0], self.future_event)
        self.assertNotIn(self.past_event, events)

    def test_companies_in_context(self):
        companies = self.response.context['companies']
        self.assertEqual(companies.count(), 2)
        self.assertTrue(self.company1 in companies)
        self.assertTrue(self.company2 in companies)

    def test_event_image_formatting(self):
        events = self.response.context['event_list']
        if events and events[0].picture:
            event = events[0]
            self.assertTrue(event.picture.name.startswith('events/'))