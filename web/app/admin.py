from django.contrib import admin
from .models import Country, MajorSubject, School, StudentSchool

admin.site.register([Country, MajorSubject, School, StudentSchool])