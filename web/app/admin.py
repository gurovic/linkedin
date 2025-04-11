from django.contrib import admin
from app.models import (
    AlumniVerificationRequest,
    Answer,
    Company,
    Event,
    Image,
    JobExperience,
    MajorSubject,
    Request,
    School,
    SkillEndorsement,
    StudentSchool,
    Skill,
    University,
    UniversityStudent,
    UserSkill,
    Vacancy,
)
from app.models.language import Language
from app.models.major import Major


@admin.action(description="Одобрить выбранные заявки")
def approve_requests(modeladmin, request, queryset):
    queryset.update(approved='AC')


@admin.action(description="Отклонить выбранные заявки")
def decline_requests(modeladmin, request, queryset):
    queryset.update(approved='DE')


@admin.register(AlumniVerificationRequest)
class AlumniVerificationRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'university', 'approved', 'date')
    list_filter = ('approved', 'university')
    actions = [approve_requests, decline_requests]



admin.site.register([MajorSubject, School, StudentSchool])
admin.site.register(Event)
admin.site.register(Vacancy)
admin.site.register(Company)
admin.site.register(Skill)
admin.site.register(Request)
admin.site.register(Answer)
admin.site.register(University)
admin.site.register(UniversityStudent)
admin.site.register(JobExperience)
admin.site.register(Image)
admin.site.register(SkillEndorsement)
admin.site.register(UserSkill)
admin.site.register(Major)
admin.site.register(Language)
