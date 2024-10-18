from django.contrib import admin
from .models.requests import Request
from .models.answer import Answer

# Register your models here.
admin.site.register(Request)
admin.site.register(Answer)