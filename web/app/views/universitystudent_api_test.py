import datetime

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import University, UniversityStudent
from app.serializers.universitystudent_serializer import (
    UniversityStudentSerializer,
)


class UniversityStudentViewTests(APITestCase):
    def setUp(self):
        self.url = reverse("universitystudent")
        self.university = University.objects.create(
            name="Test University",
            country="United States",
            majors_availible=["CS", "MATH"],
        )
        self.student1 = User.objects.create(
            username="john_doe",
        )
        self.student2 = User.objects.create(
            username="jane_smith",
        )
        self.universitystudent1 = UniversityStudent.objects.create(
            student=self.student1,
            university=self.university,
            start_year=2019,
            end_year=2023,
        )
        self.universitystudent2 = UniversityStudent.objects.create(
            student=self.student2,
            university=self.university,
            start_year=2020,
            end_year=None,
        )

    def test_get_all_university_students(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(UniversityStudentSerializer(self.universitystudent2).data, response.data)
        self.assertIn(UniversityStudentSerializer(self.universitystudent1).data, response.data)


class CurrentUniversityStudentViewTests(APITestCase):
    def setUp(self):
        self.url = reverse("current_universitystudent")
        self.university = University.objects.create(
            name="Test University",
            country="United States",
            majors_availible=["CS", "MATH"],
        )
        self.student1 = User.objects.create(
            username="john_doe",
        )
        self.student2 = User.objects.create(
            username="jane_smith",
        )
        self.student3 = User.objects.create(
            username="joe_bloggs",
        )
        self.universitystudent1 = UniversityStudent.objects.create(
            student=self.student1,
            university=self.university,
            start_year=2019,
            end_year=2023,
        )
        self.universitystudent2 = UniversityStudent.objects.create(
            student=self.student2,
            university=self.university,
            start_year=2020,
            end_year=None,
        )
        self.universitystudent3 = UniversityStudent.objects.create(
            student=self.student3,
            university=self.university,
            start_year=2018,
            end_year=datetime.datetime.now().year + 1,
        )

    def test_get_current_university_students(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(UniversityStudentSerializer(self.universitystudent2).data, response.data)
        self.assertIn(UniversityStudentSerializer(self.universitystudent3).data, response.data)
        self.assertNotIn(UniversityStudentSerializer(self.universitystudent1).data, response.data)
