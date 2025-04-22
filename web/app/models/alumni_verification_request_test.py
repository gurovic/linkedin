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
        alumni_verification_request = AlumniVerificationRequest.objects.create(
            user=self.user,
            photo="alumni_verification_request_test/kitten.jpg",
        )
        self.assertEqual(alumni_verification_request.user, self.user)
        self.assertIsNotNone(alumni_verification_request.date)
        self.assertEqual(alumni_verification_request.approved, "NA")

    def test_string_representation(self):
        alumni_verification_request = AlumniVerificationRequest.objects.create(
            user=self.user,
            photo="alumni_verification_request_test/kitten.jpg",
        )
        expected_str = f"{alumni_verification_request.user.last_name}, {alumni_verification_request.get_approved_display()}"
        self.assertEqual(str(alumni_verification_request), expected_str)

    def test_request_user_relationship(self):
        another_user = User.objects.create_user(
            username="anotheruser",
            password="anotherpass",
        )
        alumni_verification_request = AlumniVerificationRequest.objects.create(
            user=self.user,
            photo="alumni_verification_request_test/kitten.jpg",
        )
        self.assertEqual(alumni_verification_request.user.username, "testuser")
        self.assertNotEqual(
            alumni_verification_request.user.username,
            another_user.username,
        )

    def test_mail_sent_on_approved_request_with_password(self):
        alumni_password = AlumniPassword.objects.create(
            user=self.user,
            password="secret_password",
        )

        request = AlumniVerificationRequest.objects.create(user=self.user, email=self.user.email)
        request.save()
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
        request = AlumniVerificationRequest.objects.create(user=self.user, email=self.user.email)
        request.save()
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
        request = AlumniVerificationRequest.objects.create(user=self.user, email=self.user.email)
        request.approved = "DE"
        request.save()

        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]

        self.assertEqual(email.subject, "Ваш запрос на верификацию отклонен")
        self.assertEqual(email.to, [request.email])
        self.assertIn(f"Уважаемый(ая) {self.user.first_name}", email.body)
        self.assertIn("ваш запрос на верификацию был отклонен", email.body)

    def test_no_mail_sent_on_not_answered_request(self):
        request = AlumniVerificationRequest.objects.create(user=self.user)
        request.save()

        self.assertEqual(len(mail.outbox), 0)
