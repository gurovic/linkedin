from django.contrib import admin
from .models import Alumni, Employer, Event, FullName, Topic, Vacancy

# Register your models here.

admin.site.register(Alumni)
admin.site.register(Employer)
admin.site.register(Event)
admin.site.register(FullName)
admin.site.register(Topic)
admin.site.register(Vacancy)