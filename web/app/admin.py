from django.contrib import admin
from .models import Country, MajorSubject, School, StudentSchool
from .models import Request
from .models import Answer


admin.site.register([Country, MajorSubject, School, StudentSchool])
admin.site.register(Request)
admin.site.register(Answer)

