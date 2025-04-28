from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import (
    School,
    Skill,
    StudentSchool,
    University,
    UniversityStudent,
    UserSkill,
)


class SearchAPITestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username="john",
            first_name="John",
            last_name="Doe",
        )
        self.user2 = User.objects.create_user(
            username="jane",
            first_name="Jane",
            last_name="Smith",
        )

        self.university = University.objects.create(name="Test University")
        UniversityStudent.objects.create(
            student=self.user1,
            university=self.university,
        )

        self.school = School.objects.create(name="Test School")
        StudentSchool.objects.create(student=self.user1, school=self.school)

        self.skill_python = Skill.objects.create(name="Python")
        UserSkill.objects.create(user=self.user1, skill=self.skill_python)

        self.url = reverse("user_search_api")
        self.client.force_login(self.user1)

    def test_search_without_filters_returns_all_non_superusers(self):
        response = self.client.post(self.url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        first_names = [user["first_name"] for user in response.data]
        self.assertCountEqual(
            first_names,
            [self.user1.first_name, self.user2.first_name],
        )

    def test_search_by_query(self):
        response = self.client.post(self.url, {"query": "Doe"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        first_names = [user["first_name"] for user in response.data]
        self.assertEqual(first_names, [self.user1.first_name])

    def test_invalid_university(self):
        response = self.client.post(
            self.url,
            {"university": "Unknown University"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data.get("error"),
            "Invalid university name.",
        )

    def test_filter_by_university(self):
        response = self.client.post(
            self.url,
            {"university": self.university.name},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        first_names = [user["first_name"] for user in response.data]
        self.assertEqual(first_names, [self.user1.first_name])

    def test_invalid_school(self):
        response = self.client.post(
            self.url,
            {"school": "Unknown School"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("error"), "Invalid school name.")

    def test_filter_by_school(self):
        response = self.client.post(
            self.url,
            {"school": self.school.name},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        first_names = [user["first_name"] for user in response.data]
        self.assertEqual(first_names, [self.user1.first_name])

    def test_filter_by_skills(self):
        response = self.client.post(
            self.url,
            {"skills": ["Python"]},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        first_names = [user["first_name"] for user in response.data]
        self.assertEqual(first_names, [self.user1.first_name])

    def test_unauthorized(self):
        self.client.logout()
        response = self.client.post(self.url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
