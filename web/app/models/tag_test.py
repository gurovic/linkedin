from django.db.utils import IntegrityError
from django.test import TestCase

from app.models import Tag, UserTag


class TestTag(TestCase):
    def setUp(self):
        self.tag = Tag(name="example")

    def test_tag_creation(self):
        self.assertEqual(self.tag.name, "example")

    def test_tag_str(self):
        self.assertEqual(str(self.tag), "example")

class TestUserTag(TestCase):
    def setUp(self):
        self.user_tag = UserTag(user_id=1, tag_id=1)

    def test_user_tag_creation(self):
        self.assertEqual(self.user_tag.user_id, 1)
        self.assertEqual(self.user_tag.tag_id, 1)

    def test_user_tag_unique(self):
        self.user_tag.save()
        user_tag = UserTag(user_id=1, tag_id=1)
        with self.assertRaises(IntegrityError):
            user_tag.save()
