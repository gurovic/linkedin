from django.db import models

class Tag(models.Model):
    TAGS_CHOICES = [
        ("PYTHON DEVELOPER", "python developer"),
        ("WEB DESIGNER", "web designer"),
        ("C1 ENGLISH", "C1 English")
    ]
    name = models.CharField(max_length = 50, choices = TAGS_CHOICES)
    def __str__(self):
        return self.name