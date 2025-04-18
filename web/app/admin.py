from django.contrib import admin, messages
from django.core.mail import send_mail
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
import secrets
import string


@admin.action(description="Отклонить выбранные заявки")
def decline_requests(modeladmin, request, queryset):
    queryset.update(approved='DE')


@admin.action(description="Подтвердить выбранные заявки")
def confirm_and_send(modeladmin, request, queryset):
    sent_count = 0
    for obj in queryset:
        if not obj.confirmation_sent:
            password = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(10))
            send_mail(
                subject="Добро пожаловать в Город Выпускников!",
                message=f"Ваш логин: {obj.email}\nПароль: {password}",
                from_email="sue@letovo.ru",
                recipient_list=[obj.email],
                fail_silently=False,
            )
            obj.approved = 'AC'
            obj.confirmation_sent = True
            obj.save()
            sent_count += 1
    modeladmin.message_user(
        request,
        f"Подтверждено",
        messages.SUCCESS
    )


@admin.register(AlumniVerificationRequest)
class AlumniVerificationRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'university', 'approved', 'date')
    list_filter = ('approved', 'university')
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
