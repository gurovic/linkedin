from django.db import models

class Tag(models.Model):

    skill_owners = models.ManyToManyField("auth.User", blank = True, related_name = "tags")
    name = models.CharField(max_length = 150, unique = True)

    def __str__(self):
        return self.name