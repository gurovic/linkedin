from django.db import models

class Tag(models.Model):
    """TAGS_CHOICES = [
        ("PYTHON DEVELOPER", "python developer"),
        ("WEB DESIGNER", "web designer"),
        ("C1 ENGLISH", "C1 English")
    ]"""

    skill_owners = models.ManyToManyField("auth.User", related_name = "tags")
    name = models.CharField(max_length = 50)#, choices = TAGS_CHOICES)

    def is_owner(self, user_id):
        return list(self.skill_owners).count(user_id) > 0

    def __str__(self):
        return self.name