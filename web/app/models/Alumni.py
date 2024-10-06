from django.db import models

class Alumni(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    full_name = last_name.__str__() + first_name.__str__()
    friends = models.ManyToManyField("self", symmetrical=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
