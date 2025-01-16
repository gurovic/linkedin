from django.core.exceptions import ValidationError
from django.db import models


class SkillEndorsement(models.Model):
    endorser = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    usertag = models.ForeignKey("UserSkill", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.endorser} endorsed {self.usertag}"

    def clean(self):
        # Validate unique endorsement
        if SkillEndorsement.objects.filter(
            endorser=self.endorser,
            usertag=self.usertag,
        ).exists():
            raise ValidationError("Endorsement already exists")

        # Validate self endorsement
        if self.usertag.user == self.endorser:
            raise ValidationError("You cannot endorse your own skill")

        super().clean()