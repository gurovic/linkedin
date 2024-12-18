from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from app.models import UserTag
from app.models.skill_endorsement import SkillEndorsement
from app.models.tag import Tag


class SkillEndorsementTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="user1")
        self.user2 = User.objects.create(username="user2")
        self.tag = Tag.objects.create(name="Python")
        self.usertag1 = UserTag.objects.create(user=self.user1, tag=self.tag)

    def test_create_skill_endorsement(self):
        endorsement = SkillEndorsement.objects.create(
            endorser=self.user1,
            usertag=self.usertag1,
        )
        self.assertEqual(endorsement.endorser, self.user1)
        self.assertEqual(endorsement.usertag, self.usertag1)

    def test_unique_endorsement_validation(self):
        SkillEndorsement.objects.create(endorser=self.user1, usertag=self.usertag1)
        with self.assertRaises(ValidationError):
            endorsement = SkillEndorsement(endorser=self.user1, usertag=self.usertag1)
            endorsement.full_clean()

    def test_self_endorsement_validation(self):
        with self.assertRaises(ValidationError):
            endorsement = SkillEndorsement(endorser=self.user1, usertag=self.usertag1)
            endorsement.full_clean()
