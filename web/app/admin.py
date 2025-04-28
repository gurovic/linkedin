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
    Skill,
    SkillEndorsement,
    StudentSchool,
    University,
    UniversityStudent,
    UserSkill,
    Vacancy,
)
from app.models.alumnipassword import AlumniPassword
from app.models.language import Language
from app.models.major import Major


@admin.action(description="Отклонить выбранные заявки")
def decline_requests(modeladmin, request, queryset):
    for obj in queryset:
        obj.approved = "DE"
        obj.save()


@admin.action(description="Подтвердить выбранные заявки")
def confirm_and_send(modeladmin, request, queryset):
    for obj in queryset:
        obj.approved = "AC"
        obj.save()


@admin.register(AlumniVerificationRequest)
class AlumniVerificationRequestAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "university", "approved", "date")
    list_filter = ("approved", "university")
    actions = [decline_requests, confirm_and_send]

    @admin.display(description="ФИО")
    def full_name(self, obj):
        parts = [obj.surname, obj.first_name, obj.middle_name]
        return " ".join(filter(None, parts))


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
admin.site.register(AlumniPassword)
