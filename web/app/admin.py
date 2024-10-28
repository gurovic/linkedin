from django.contrib import admin
from .models import Vacancy, Company, Request, Answer

# Register your models here.
admin.site.register(Vacancy)
admin.site.register(Company)
admin.site.register(Request)
admin.site.register(Answer)
