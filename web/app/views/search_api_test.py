from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import School, StudentSchool, University, UniversityStudent


class UserSearchAPITestCase(APITestCase):
    def setUp(self):
        self.url = reverse("user_search_api")
        self.user1 = User.objects.create(
            first_name="John",
            last_name="Doe",
            username="johndoe",
        )
        self.user2 = User.objects.create(
            first_name="Jane",
            last_name="Smith",
            username="janesmith",
        )
        self.university = University.objects.create(name="Test University")
        self.school = School.objects.create(name="Test School")
        UniversityStudent.objects.create(
            student=self.user1,
            university=self.university,
        )
        StudentSchool.objects.create(student=self.user2, school=self.school)

    def test_search_by_query(self):
        response = self.client.get(self.url, {"query": "John"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["first_name"], "John")

    def test_search_by_university(self):
        response = self.client.get(
            self.url,
            {"university": self.university.id},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["first_name"], "John")

    def test_search_by_school(self):
        response = self.client.get(self.url, {"school": self.school.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["first_name"], "Jane")

    def test_search_by_query_and_university(self):
        response = self.client.get(
            self.url,
            {"query": "John", "university": self.university.id},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["first_name"], "John")

    def test_search_by_query_and_school(self):
        response = self.client.get(
            self.url,
            {"query": "Jane", "school": self.school.id},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["first_name"], "Jane")
