from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from app.models import Userskill
from app.models.skill_endorsement import SkillEndorsement
from app.models.skill import skill


class SkillEndorsementTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="user1")
        self.user2 = User.objects.create(username="user2")
        self.skill = skill.objects.create(name="Python")
        self.userskill1 = Userskill.objects.create(user=self.user1, skill=self.skill)

    def test_create_skill_endorsement(self):
        endorsement = SkillEndorsement.objects.create(
            endorser=self.user1,
            userskill=self.userskill1,
        )
        self.assertEqual(endorsement.endorser, self.user1)
        self.assertEqual(endorsement.userskill, self.userskill1)

    def test_unique_endorsement_validation(self):
        SkillEndorsement.objects.create(endorser=self.user1, userskill=self.userskill1)
        with self.assertRaises(ValidationError):
            endorsement = SkillEndorsement(endorser=self.user1, userskill=self.userskill1)
            endorsement.full_clean()

    def test_self_endorsement_validation(self):
        with self.assertRaises(ValidationError):
            endorsement = SkillEndorsement(endorser=self.user1, userskill=self.userskill1)
            endorsement.full_clean()
