from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models.useraccount import UserAccount
from .models import Request
from .models import Answer


class UserAccountResource(resources.ModelResource):
    class Meta:
        model = UserAccount


class UseraccAdmin(ImportExportModelAdmin):
    resource_classes = [UserAccountResource]


admin.site.register(UserAccount, UseraccAdmin)
admin.site.register(Request)
admin.site.register(Answer)
