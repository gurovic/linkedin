from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from app.models import University, UniversityStudent, StudentSchool, School


class UserSearchViewTests(TestCase):
    def setUp(self):
        self.university1 = University.objects.create(name="Harvard University")
        self.university2 = University.objects.create(
            name="Stanford University",
        )

        self.school1 = School.objects.create(country="Russian Federation", name="Letovo School")
        self.school2 = School.objects.create(country="United States", name="Utah High School Real")

        self.user1 = User.objects.create_user(
            username="testuser1",
            first_name="Stephen",
            last_name="Curry",
        )
        self.user2 = User.objects.create_user(
            username="testuser2",
            first_name="Kevin",
            last_name="Durant",
        )
        self.user3 = User.objects.create_user(
            username="testuser3",
            first_name="James",
            last_name="LeBron",
        )

        UniversityStudent(
            university=self.university1,
            student=self.user1,
            start_year="2025",
        ).save()
        UniversityStudent(
            university=self.university2,
            student=self.user2,
            start_year="2025",
        ).save()
        UniversityStudent(
            university=self.university1,
            student=self.user3,
            start_year="2025",
        ).save()

        StudentSchool(
            school=self.school1,
            student=self.user1,
            start_year="2021"
        ).save()
        StudentSchool(
            school=self.school1,
            student=self.user2,
            start_year="2020"
        ).save()
        StudentSchool(
            school=self.school2,
            student=self.user3,
            start_year="2022"
        ).save()

    def test_last_name(self):
        response = self.client.get(reverse("user_search"), {"query": "curry"})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Stephen Curry")
        self.assertNotContains(response, "Kevin Durant")
        self.assertNotContains(response, "James LeBron")

    def test_first_name(self):
        response = self.client.get(reverse("user_search"), {"query": "Steph"})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Stephen Curry")
        self.assertNotContains(response, "Kevin Durant")
        self.assertNotContains(response, "James LeBron")

    def test_first_last_name(self):
        response = self.client.get(
            reverse("user_search"),
            {"query": "Stephen curry"},
        )
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Stephen Curry")

    def test_last_first_name(self):
        response = self.client.get(
            reverse("user_search"),
            {"query": "curry Stephen"},
        )
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Stephen Curry")

    def test_partial_query(self):
        response = self.client.get(
            reverse("user_search"),
            {"query": "   EN Cu "},
        )
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Stephen Curry")
        self.assertNotContains(response, "Kevin Durant")
        self.assertNotContains(response, "James LeBron")

    def test_no_results(self):
        response = self.client.get(reverse("user_search"), {"query": "Russ"})
        self.assertEqual(response.status_code, 200)

        self.assertNotContains(response, "Stephen Curry")
        self.assertContains(response, "No users found.")

    def test_empty_query(self):
        response = self.client.get(reverse("user_search"), {"query": "   "})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Stephen Curry")

    def test_multiple_results(self):
        response = self.client.get(reverse("user_search"), {"query": "a"})
        self.assertEqual(response.status_code, 200)

        self.assertNotContains(response, "Stephen Curry")
        self.assertContains(response, "Kevin Durant")
        self.assertContains(response, "James LeBron")

    def test_search_by_university(self):
        response = self.client.get(
            reverse("user_search"),
            {"university": self.university1.id},
        )
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Stephen Curry")
        self.assertContains(response, "James LeBron")
        self.assertNotContains(response, "Kevin Durant")

    def test_search_by_university_no_results(self):
        response = self.client.get(
            reverse("user_search"),
            {"university": self.university2.id},
        )
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Kevin Durant")
        self.assertNotContains(response, "Stephen Curry")
        self.assertNotContains(response, "James LeBron")
    
    def test_search_by_school(self):
        response = self.client.get(
            reverse("user_search"),
            {"school": self.school1.id},
        )
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Stephen Curry")
        self.assertContains(response, "Kevin Durant")
        self.assertNotContains(response, "James LeBron")

    def test_search_by_school_no_results(self):
        response = self.client.get(
            reverse("user_search"),
            {"school": self.school2.id},
        )
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "James LeBron")
        self.assertNotContains(response, "Stephen Curry")
        self.assertNotContains(response, "Kevin Durant")

    def test_combined_filters(self):
        response = self.client.get(
            reverse("user_search"),
            {"query": "Stephen", "university": self.university1.id, "school": self.school1.id},
        )
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Stephen Curry")
        self.assertNotContains(response, "Kevin Durant")
        self.assertNotContains(response, "James LeBron")
