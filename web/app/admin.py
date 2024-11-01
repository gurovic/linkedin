from django.contrib import admin
from .models import MajorSubject, School, StudentSchool
from .models import Vacancy, Company, Request, Answer, Tag, JobExperience

admin.site.register([MajorSubject, School, StudentSchool])
admin.site.register(Request)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(Vacancy)
admin.site.register(Company)
admin.site.register(JobExperience)