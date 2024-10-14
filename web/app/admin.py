from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models.alumni import Friend
from .models.useracc import Useracc


# Register your models here.
class UseraccResource(resources.ModelResource):
    class Meta:
        model = Useracc


class UseraccAdmin(ImportExportModelAdmin):
    resource_classes = [UseraccResource]


myModels = [Friend]
admin.site.register(myModels)
admin.site.register(Useracc, UseraccAdmin)
