from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.utils import timezone
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
import io

from app.models import AlumniVerificationRequest

class ApiAnsVerificationTestView(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass",
        )
        self.client.force_authenticate(user=self.user)
        self.ans_without_photo = AlumniVerificationRequest.objects.create(
            user=self.user,
            date=timezone.now(),
            approved='NA',
        )
        img = Image.new('RGB', (100, 100), color='green')
        image_io = io.BytesIO()
        img.save(image_io, format='JPEG')
        self.ans_with_photo = AlumniVerificationRequest.objects.create(
            user=self.user,
            date=timezone.now(),
            image=SimpleUploadedFile('test_image.jpg', image_io.getvalue(), content_type='image/jpeg'),
            approved='NA',
        )

    def create_answer(self):
        self.assertEqual(self.ans_without_photo.user, self.user)
        self.assertAlmostEqual(self.ans_without_photo.date, timezone.now(), delta=timezone.timedelta(seconds=2))
        self.assertEqual(self.ans_without_photo.approved, 'NA')

    def modify_status(self):
        self.ans_without_photo.name = 'DE'
        self.ans_without_photo.save()
        updated_ans = AlumniVerificationRequest.objects.get(id=self.ans_without_photo.id)
        self.assertEqual(updated_ans.name, 'DE')