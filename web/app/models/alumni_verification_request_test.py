import datetime
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from app.models.alumni_verification_request import AlumniVerificationRequest

class AlumniVerificationRequestModelTest(TestCase):

    def setUp(self):
        self.request = AlumniVerificationRequest.objects.create(
            surname="Smith",
            first_name="John",
            middle_name="Edward",
            email="john.smith@example.com",
            university="MIT"
        )

    def test_instance_created(self):
        self.assertEqual(self.request.surname, "Smith")
        self.assertEqual(self.request.first_name, "John")
        self.assertEqual(self.request.middle_name, "Edward")
        self.assertEqual(self.request.email, "john.smith@example.com")
        self.assertEqual(self.request.university, "MIT")

    def test_default_values(self):
        today = datetime.date.today()
        self.assertEqual(self.request.date, today)
        self.assertEqual(self.request.approved, 'NA')
        self.assertFalse(self.request.confirmation_sent)

    def test_str_representation(self):
        expected_str = "Smith John, Not answered"
        self.assertEqual(str(self.request), expected_str)

    def test_upload_photo(self):
        image = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
        self.request.photo = image
        self.request.save()
        self.assertTrue(self.request.photo.name.startswith("verif/test.jpg"))
