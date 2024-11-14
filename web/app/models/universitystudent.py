from django.db import models
from django.contrib.auth.models import User
from .university import University


class UniversityStudent(models.Model):
    LEAVE_REASON_CHOICES = [
        ('TRANSFER', 'Transfer to another institution'),
        ('GRADUATION', 'Graduation'),
        ('PERSONAL', 'Personal reasons'),
        ('ACADEMIC', 'Academic issues'),
        ('FINANCIAL', 'Financial issues'),
        ('OTHER', 'Other'),
    ]

    student_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    university_id = models.ForeignKey(University,on_delete=models.CASCADE, related_name='university_students')
    leave_reason = models.CharField(null=True, blank=True, max_length=20, choices=LEAVE_REASON_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student_id.username} - {self.university_id}"