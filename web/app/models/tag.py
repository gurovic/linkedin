from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class UserTag(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "tag")

    def __str__(self):
        return f"{self.user.username} - {self.tag.name}"
