from django.contrib import admin
from .models import Vacancy,Company

admin.site.register([Vacancy,Company])
