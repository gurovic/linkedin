from django.db import models
from django.contrib.auth.models import User
from .university import University
from django.core.exceptions import ValidationError
from ..utils import get_year

class UniversityStudent(models.Model):
    LEAVE_REASON_CHOICES = [
        ('TRANSFER', 'Transfer to another institution'),
        ('GRADUATION', 'Graduation'),
        ('PERSONAL', 'Personal reasons'),
        ('ACADEMIC', 'Academic issues'),
        ('FINANCIAL', 'Financial issues'),
        ('OTHER', 'Other'),
    ]

    LEVEL = [
        ('BACHELOR', 'Bachelor\'s degree'),
        ('MASTER', 'Master\'s degree'),
        ('SPECIALIST', 'Specialist\'s degree'),
        ('PhD', 'PhD/Аспирантура'),
        ('DOCTORAL', 'Doctoral studies'),
        ('MBA', 'Master of Business Administration'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    university = models.ForeignKey(University,on_delete=models.CASCADE, related_name='university_students')
    leave_reason = models.CharField(null=True, blank=True, max_length=20, choices=LEAVE_REASON_CHOICES)
    start_year = models.PositiveIntegerField(
        default=get_year,
        help_text="Select the year when the program started",
    )
    end_year = models.PositiveIntegerField(
        null=True, 
        blank=True,
        help_text="Select the year when the program ended (optional)"
    )

    def __str__(self):
        return f"{self.student.username} - {self.university}"

    def clean(self):
        if self.end_year and self.start_year and self.end_year <= self.start_year:
            raise ValidationError({"end_year": "End year must be after start year."})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
