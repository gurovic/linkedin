from django.contrib import admin
from .models import Vacancy, MajorSubject, Company, Country

admin.site.register([Vacancy, MajorSubject, Company, Country])
