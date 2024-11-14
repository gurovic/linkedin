from django.contrib import admin
from .models import Vacancy, Company, Request, Answer, University, UniversityStudent

# Register your models here.
admin.site.register(Vacancy)
admin.site.register(Company)
admin.site.register(Request)
admin.site.register(Answer)
admin.site.register(University)
admin.site.register(UniversityStudent)