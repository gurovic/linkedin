from django.contrib import admin

# Register your models here.
from .models import Tag
from .models import TagUser
admin.site.register(Tag)
admin.site.register(TagUser)