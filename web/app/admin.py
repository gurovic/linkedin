from django.contrib import admin
from .models.alumni import Friend
# Register your models here.
myModels = [Friend]
admin.site.register(myModels)
