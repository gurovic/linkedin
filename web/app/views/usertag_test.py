from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import SkillEndorsement, Tag, UserTag


class UserTagViewTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="testuser1", password="password")
        self.client.login(username="testuser1", password="password")

        self.tag = Tag.objects.create(name="Test Tag")
        self.tag2 = Tag.objects.create(name="Test Tag 2")
        self.user_tag = UserTag.objects.create(user=self.user1, tag=self.tag)

    def test_list_user_tags(self):
        url = f"/api/user/{self.user1.id}/skills/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["tag"], 1)

    def test_create_user_tag(self):
        url = f"/api/user/{self.user1.id}/skills/"
        response = self.client.post(url, {"tag": 2})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserTag.objects.count(), 2)

    def test_delete_user_tags(self):
        url = f"/api/user/{self.user1.id}/skill/{self.tag.id}/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(UserTag.objects.count(), 0)


class SkillEndorsementAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password"
        )
        self.tag = Tag.objects.create(name="Test Tag")
        self.client.login(username="testuser", password="password")
        self.user2 = User.objects.create_user(
            username="testuser2", password="password"
        )
        self.user_tag = UserTag.objects.create(user_id=self.user2.id, tag_id=1)

    def test_list_skill_endorsements(self):
        SkillEndorsement.objects.create(
            endorser=self.user, usertag=self.user_tag
        )
        url = f"/api/user/{self.user2.id}/skill/{self.user_tag.id}/endorsement/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["endorser"], "testuser")

    def test_endorse_skill(self):
        url = f"/api/user/{self.user2.id}/skill/{self.user_tag.id}/endorsement/"
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SkillEndorsement.objects.count(), 1)

    def test_endorse_skill_already_exists(self):
        SkillEndorsement.objects.create(
            endorser=self.user, usertag=self.user_tag
        )
        url = f"/api/user/{self.user2.id}/skill/{self.user_tag.id}/endorsement/"
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Endorsement already exists", response.data["error"])

    def test_endorse_skill_invalid_user_or_skill(self):
        url = "/api/user/999/skill/999/endorsement/"
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_skill_endorsement(self):
        SkillEndorsement.objects.create(
            endorser=self.user, usertag=self.user_tag
        )
        url = f"/api/user/{self.user2.id}/skill/{self.user_tag.id}/endorsement/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SkillEndorsement.objects.count(), 0)
