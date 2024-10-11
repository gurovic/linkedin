from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=128)
    profession = models.CharField(max_length=128)  #? Create class Profession and add many-to-one connection
    description = models.TextField()

    # company = models.ForeignKey(Company, on_delete=models.CASCADE) #? Will we have class Company

    date_of_creation = models.DateTimeField()
    # ToDo: candidates = models.ManyToManyField("", related_name="candidates")

    def __str__(self):
        return self.title

