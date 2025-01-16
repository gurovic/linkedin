from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from app.models import Tag, UserTag


class TestTagViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.tag1 = Tag.objects.create(name="Tag1")
        self.tag2 = Tag.objects.create(name="Tag2")
        self.usertag = UserTag.objects.create(user=self.user, tag=self.tag1)

    def test_add_tag_to_user_get(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("add_tags"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertNotIn(
            self.tag1, response.context["form"].fields["tag"].queryset
        )
        self.assertIn(
            self.tag2, response.context["form"].fields["tag"].queryset
        )

    def test_add_tag_to_user_post(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse("add_tags"), {"tag": self.tag2.id})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            UserTag.objects.filter(user=self.user, tag=self.tag2).exists()
        )

    def test_tags_view(self):
        response = self.client.get(
            reverse("user_tags_old", args=[self.user.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("usertags_list", response.context)
        self.assertIn(self.usertag, response.context["usertags_list"])
