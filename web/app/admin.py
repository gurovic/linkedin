from django.contrib import admin
from .models.requests import Request
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Request)
admin.site.register(User)
