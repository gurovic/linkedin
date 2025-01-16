from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from app.models import skill, Userskill


class TestskillViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.skill1 = skill.objects.create(name="skill1")
        self.skill2 = skill.objects.create(name="skill2")
        self.userskill = Userskill.objects.create(user=self.user, skill=self.skill1)

    def test_add_skill_to_user_get(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("add_skills"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertNotIn(
            self.skill1, response.context["form"].fields["skill"].queryset
        )
        self.assertIn(
            self.skill2, response.context["form"].fields["skill"].queryset
        )

    def test_add_skill_to_user_post(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse("add_skills"), {"skill": self.skill2.id})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Userskill.objects.filter(user=self.user, skill=self.skill2).exists()
        )

    def test_skills_view(self):
        response = self.client.get(
            reverse("user_skills_old", args=[self.user.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("userskills_list", response.context)
        self.assertIn(self.userskill, response.context["userskills_list"])
