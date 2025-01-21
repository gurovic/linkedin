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
admin.site.register(AlumniVerificationRequest)
admin.site.register(Image)
admin.site.register(SkillEndorsement)
admin.site.register(UserSkill)
