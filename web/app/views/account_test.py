from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from app.models import (
    MajorSubject,
    School,
    StudentSchool,
    University,
    UniversityStudent,
)


class AccountViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            username="testuser1",
            email="testuser1@example.com",
            password="testpassword",
            first_name="Name1",
            last_name="Surname1",
        )
        self.user2 = User.objects.create_user(
            username="testuser2",
            email="testuser2@example.com",
            password="testpassword",
            first_name="Name2",
            last_name="Surname2",
        )

        self.school1 = School.objects.create(
            name="Test School 1",
            country="RU",
        )
        self.school2 = School.objects.create(
            name="Test School 2",
            country="US",
        )
        self.major1 = MajorSubject.objects.create(subject="CS")
        self.major2 = MajorSubject.objects.create(subject="MATH")
        self.school1.majors.add(self.major1, self.major2)
        self.school2.majors.add(self.major1)
        self.university1 = University.objects.create(
            name="Test University 1",
            country="RU",
        )
        self.university2 = University.objects.create(
            name="Test University 2",
            country="US",
        )

        self.student_school1 = StudentSchool.objects.create(
            student=self.user1,
            school=self.school1,
            start_year=2018,
            finish_year=2022,
            why_left="GR",
        )
        self.student_school2 = StudentSchool.objects.create(
            student=self.user2,
            school=self.school2,
            start_year=2016,
            finish_year=2020,
            why_left="EX",
        )
        self.university_student1 = UniversityStudent.objects.create(
            student=self.user1,
            university=self.university1,
            start_year=2020,
            end_year=2024,
            leave_reason="GRADUATION",
        )
        self.university_student2 = UniversityStudent.objects.create(
            student=self.user2,
            university=self.university2,
            start_year=2018,
            end_year=2022,
            leave_reason="TRANSFER",
        )

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.major1.delete()
        self.major2.delete()
        self.school1.delete()
        self.school2.delete()
        self.university1.delete()
        self.university2.delete()
        self.student_school1.delete()
        self.student_school2.delete()
        self.university_student1.delete()
        self.university_student2.delete()

    def test_account_view_for_current_user(self):
        self.client.login(username="testuser1", password="testpassword")
        response = self.client.get(
            reverse("uneditable_account", args=[self.user1.id]),
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.user1.first_name)
        self.assertContains(response, self.user1.last_name)
        self.assertContains(response, self.user1.username)
        self.assertContains(response, self.user1.email)
        self.assertContains(response, "Test School 1")
        self.assertContains(response, "Test University 1")

    def test_account_view_for_other_user(self):
        self.client.login(username="testuser1", password="testpassword")
        response = self.client.get(
            reverse("uneditable_account", args=[self.user2.id]),
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.user2.first_name)
        self.assertContains(response, self.user2.last_name)
        self.assertContains(response, self.user2.username)
        self.assertContains(response, self.user2.email)
        self.assertContains(response, "Test School 2")
        self.assertContains(response, "Test University 2")

    def test_unediatble_account_view_context(self):
        self.client.login(username="testuser1", password="testpassword")
        response = self.client.get(
            reverse("uneditable_account", args=[self.user2.id]),
        )
        self.assertEqual(response.context["user"], self.user2)
        self.assertIn(
            self.student_school2,
            response.context["student_schools"],
        )
        self.assertIn(
            self.university_student2,
            response.context["student_universities"],
        )


class EditableAccountViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            username="testuser1",
            email="testuser1@example.com",
            password="testpassword",
            first_name="Name1",
            last_name="Surname1",
        )
        self.user2 = User.objects.create_user(
            username="testuser2",
            email="testuser2@example.com",
            password="testpassword",
            first_name="Name2",
            last_name="Surname2",
        )

        self.school1 = School.objects.create(
            name="Test School 1",
            country="RU",
        )
        self.school2 = School.objects.create(
            name="Test School 2",
            country="US",
        )
        self.major1 = MajorSubject.objects.create(subject="CS")
        self.major2 = MajorSubject.objects.create(subject="MATH")
        self.school1.majors.add(self.major1, self.major2)
        self.school2.majors.add(self.major1)
        self.university1 = University.objects.create(
            name="Test University 1",
            country="RU",
        )
        self.university2 = University.objects.create(
            name="Test University 2",
            country="US",
        )

        self.student_school1 = StudentSchool.objects.create(
            student=self.user1,
            school=self.school1,
            start_year=2018,
            finish_year=2022,
            why_left="GR",
        )
        self.student_school2 = StudentSchool.objects.create(
            student=self.user2,
            school=self.school2,
            start_year=2016,
            finish_year=2020,
            why_left="EX",
        )
        self.university_student1 = UniversityStudent.objects.create(
            student=self.user1,
            university=self.university1,
            start_year=2020,
            end_year=2024,
            leave_reason="GRADUATION",
        )
        self.university_student2 = UniversityStudent.objects.create(
            student=self.user2,
            university=self.university2,
            start_year=2018,
            end_year=2022,
            leave_reason="TRANSFER",
        )

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.major1.delete()
        self.major2.delete()
        self.school1.delete()
        self.school2.delete()
        self.university1.delete()
        self.university2.delete()
        self.student_school1.delete()
        self.student_school2.delete()
        self.university_student1.delete()
        self.university_student2.delete()

    def test_access_negative(self):
        self.client.login(username="testuser2", password="testpassword")
        response = self.client.get(
            reverse("editable_account", args=[self.user1.id]),
        )
        self.assertRedirects(
            response, reverse("uneditable_account", args=[self.user1.id])
        )

    def test_access_positive(self):
        self.client.login(username="testuser1", password="testpassword")
        response = self.client.get(
            reverse("editable_account", args=[self.user1.id]),
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        
    def test_contents(self):
        self.client.login(username="testuser1", password="testpassword")
        response = self.client.get(
            reverse("editable_account", args=[self.user1.id]),
        )
        self.assertContains(response, self.user1.username)
        self.assertContains(response, self.user1.email)
        self.assertContains(response, "Университеты")
        self.assertContains(response, "Школы")
        self.assertContains(response, "Сменить пароль")
