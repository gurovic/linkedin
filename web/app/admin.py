from django.contrib import admin
from .models import Request
from .models import Answer
from .models import Event
from .models import Tag

# Register your models here.
admin.site.register(Event)
admin.site.register(Tag)
admin.site.register(Request)
admin.site.register(Answer)
