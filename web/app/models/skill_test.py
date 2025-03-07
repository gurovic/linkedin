from django.db.utils import IntegrityError
from django.test import TestCase

from app.models import Skill, UserSkill


class Testskill(TestCase):
    def setUp(self):
        self.skill = Skill(name="example")

    def test_skill_creation(self):
        self.assertEqual(self.skill.name, "example")

    def test_skill_str(self):
        self.assertEqual(str(self.skill), "example")

class TestUserSkill(TestCase):
    def setUp(self):
        self.user_skill = UserSkill(user_id=1, skill_id=1)

    def test_user_skill_creation(self):
        self.assertEqual(self.user_skill.user_id, 1)
        self.assertEqual(self.user_skill.skill_id, 1)

    def test_user_skill_unique(self):
        self.user_skill.save()
        user_skill = UserSkill(user_id=1, skill_id=1)
        with self.assertRaises(IntegrityError):
            user_skill.save()
