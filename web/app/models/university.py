from django.db import models
from multiselectfield import MultiSelectField
from django.core.exceptions import ValidationError


class University(models.Model):
    COUNTRY_CHOICES = [
        ('RU', 'Russian Federation'),
        ('US', 'United States'),
        ('CA', 'Canada'),
        ('GB', 'United Kingdom'),
        ('DE', 'Germany'),
        ('FR', 'France'),
        ('JP', 'Japan'),
        ('CN', 'China'),
        ('IN', 'India'),
        ('BR', 'Brazil'),
    ]
    MAJOR_CHOICES = [
        ('CS', 'Computer Science'),
        ('MATH', 'Mathematics'),
        ('ENG', 'English'),
        ('RU', 'Russian Language'),
        ('ART', 'Arts'),
        ('BIO', 'Biology'),
        ('PHY', 'Physics'),
        ('CHEM', 'Chemistry'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=100, default='Smth', choices=COUNTRY_CHOICES)
    majors_availible = MultiSelectField(max_length=100, default='Smth', choices=MAJOR_CHOICES)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    country = models.CharField(max_length=100, blank=True)

    '''The script country_from_coords is required for the code to work properly

    def get_country_from_coords(self):
        if self.lat is not None and self.lon is not None:
            try:
                from country_from_coords import get_country
                return get_country(self.lat, self.lon) 
            except ImportError:
                raise ValidationError("The script country_from_coords.py is missing!")

    def save(self, *args, **kwargs):
        if not self.country and self.lat is not None and self.lon is not None:
            self.country = self.get_country_from_coords()
        super().save(*args, **kwargs)
    
    '''

    def __str__(self):
        return self.name
