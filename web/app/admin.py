from django.contrib import admin
from .models import Vacancy, MajorSubject, Company, Country
from .models.requests import Request

# Register your models here.
admin.site.register([Vacancy, MajorSubject, Company, Country, Request])