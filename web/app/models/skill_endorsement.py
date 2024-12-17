from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class SkillEndorsement(models.Model):
    endorser = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey("UserTag", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.endorser} endorsed {self.skill}"

    def clean(self):
        # Validate unique endorsement
        if SkillEndorsement.objects.filter(
            endorser=self.endorser,
            skill=self.skill,
        ).exists():
            raise ValidationError("Endorsement already exists")

        # Validate self endorsement
        if self.skill.user == self.endorser:
            raise ValidationError("You cannot endorse your own skill")

        super().clean()