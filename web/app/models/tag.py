from django.db import models

class Tag(models.Model):

    skill_owners = models.ManyToManyField("auth.User", related_name = "tags")
    name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.name