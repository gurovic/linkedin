from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.test import TestCase

from app.models.alumnipassword import AlumniPassword


class AlumniPasswordTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )
        self.alumni_password = AlumniPassword.objects.create(
            user=self.user,
            password="alumni_secret_password",
        )

    def test_alumni_password_creation(self):
        self.assertEqual(AlumniPassword.objects.count(), 1)
        self.assertEqual(self.alumni_password.user, self.user)
        self.assertEqual(
            self.alumni_password.password,
            "alumni_secret_password",
        )

    def test_alumni_password_string_representation(self):
        expected_str = f"{self.user.username} - пароль незарегистрированного"
        self.assertEqual(str(self.alumni_password), expected_str)

    def test_alumni_password_update(self):
        new_password = "new_alumni_password"
        self.alumni_password.password = new_password
        self.alumni_password.save()

        updated_alumni_password = AlumniPassword.objects.get(
            pk=self.alumni_password.pk,
        )
        self.assertEqual(updated_alumni_password.password, new_password)

    def test_alumni_password_delete(self):
        self.alumni_password.delete()
        self.assertEqual(AlumniPassword.objects.count(), 0)

    def test_user_alumni_password_relationship(self):
        self.assertEqual(self.user.alumnipassword, self.alumni_password)

    def test_cascade_delete(self):
        self.user.delete()
        self.assertEqual(AlumniPassword.objects.count(), 0)

    def test_uniqueness_per_user(self):
        with self.assertRaises(IntegrityError):
            AlumniPassword.objects.create(
                user=self.user,
                password="another_password",
            )
