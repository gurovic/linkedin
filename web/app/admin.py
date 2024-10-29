from django.contrib import admin
from .models import Request
from .models import Answer

# Register your models here.
from .models import Tag
admin.site.register(Tag)
admin.site.register(Request)
admin.site.register(Answer)
