from django.contrib import admin
from .models import MajorSubject, School, StudentSchool
from .models import Request
from .models import Answer


admin.site.register([MajorSubject, School, StudentSchool])
admin.site.register(Request)
admin.site.register(Answer)

