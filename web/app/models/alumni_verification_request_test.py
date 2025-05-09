from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from django.test.utils import override_settings

from app.models.alumni_verification_request import AlumniVerificationRequest
from app.models.alumnipassword import AlumniPassword


@override_settings(
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
)
class AlumniVerificationRequestTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass",
            email="testuser@example.com",
            first_name="Иван",
            last_name="Иванов",
        )

    def test_create_request(self):
        request = AlumniVerificationRequest.objects.create(
            user=self.user,
            email="alumni@example.com",
            university="Test University",
            photo="verif/kitten.jpg",
        )
        self.assertEqual(request.user, self.user)
        self.assertEqual(request.email, "alumni@example.com")
        self.assertEqual(request.university, "Test University")
        self.assertEqual(request.approved, "NA")
        self.assertFalse(request.confirmation_sent)
        self.assertIsNotNone(request.date)

    def test_string_representation(self):
        request = AlumniVerificationRequest.objects.create(
            user=self.user,
            surname="Петров",
            first_name="Петр",
            email="petrov@example.com",
            university="МГУ",
        )
        expected_str = f"Петров Петр, {request.get_approved_display()}"
        self.assertEqual(str(request), expected_str)

    def test_request_user_relationship(self):
        another_user = User.objects.create_user(
            username="anotheruser",
            password="anotherpass",
        )
        request = AlumniVerificationRequest.objects.create(
            user=self.user,
            email="testuser@example.com",
            university="Test University",
        )
        self.assertEqual(request.user.username, "testuser")
        self.assertNotEqual(request.user.username, another_user.username)

    def test_mail_sent_on_approved_request_with_password(self):
        AlumniPassword.objects.create(
            user=self.user,
            password="secret_password",
        )

        request = AlumniVerificationRequest.objects.create(
            user=self.user,
            email=self.user.email,
            university="Test University"
        )
        request.approved = "AC"
        request.save()

        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]

        self.assertEqual(email.subject, "Ваш запрос на верификацию одобрен")
        self.assertEqual(email.to, [request.email])
        self.assertIn(f"Уважаемый(ая) {self.user.first_name}", email.body)
        self.assertIn("Ваш запрос на верификацию был одобрен", email.body)
        self.assertIn("Имя пользователя: testuser", email.body)
        self.assertIn("Пароль: secret_password", email.body)

    def test_mail_sent_on_approved_request_without_password(self):
        request = AlumniVerificationRequest.objects.create(
            user=self.user,
            email=self.user.email,
            university="Test University"
        )
        request.approved = "AC"
        request.save()

        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]

        self.assertEqual(email.subject, "Ваш запрос на верификацию одобрен")
        self.assertEqual(email.to, [request.email])
        self.assertIn(f"Уважаемый(ая) {self.user.first_name}", email.body)
        self.assertIn("Ваш запрос на верификацию был одобрен", email.body)
        self.assertNotIn("Ваши учетные данные для входа", email.body)
        self.assertNotIn("Пароль:", email.body)

    def test_mail_sent_on_declined_request(self):
        request = AlumniVerificationRequest.objects.create(
            user=self.user,
            email=self.user.email,
            university="Test University"
        )
        request.approved = "DE"
        request.save()

        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]

        self.assertEqual(email.subject, "Ваш запрос на верификацию отклонен")
        self.assertEqual(email.to, [request.email])
        self.assertIn(f"Уважаемый(ая) {self.user.first_name}", email.body)
        self.assertIn("ваш запрос на верификацию был отклонен", email.body)
