from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models.useraccount import UserAccount


# Register your models here.
class UserAccountResource(resources.ModelResource):
    class Meta:
        model = UserAccount


class UseraccAdmin(ImportExportModelAdmin):
    resource_classes = [UserAccountResource]


admin.site.register(UserAccount, UseraccAdmin)