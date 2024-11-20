from django.contrib import admin
from .models import MajorSubject, School, StudentSchool, Vacancy, Company, Request, Answer, Tag, JobExperience, Event

admin.site.register([MajorSubject, School, StudentSchool])
admin.site.register(Event)
admin.site.register(Vacancy)
admin.site.register(Company)
admin.site.register(Tag)
admin.site.register(Request)
admin.site.register(Answer)
admin.site.register(JobExperience)
