from django.contrib import admin
from .models import Vacancy, Company, Request, Answer, Tag, JobExperience

admin.site.register(Vacancy)
admin.site.register(Company)
admin.site.register(Tag)
admin.site.register(Request)
admin.site.register(Answer)
admin.site.register(JobExperience)