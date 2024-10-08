from django.contrib import admin
from .models.requests import Request
from .models.rights import Right
from .models.user import User

# Register your models here.
admin.site.register(Request)
admin.site.register(User)
admin.site.register(Right)