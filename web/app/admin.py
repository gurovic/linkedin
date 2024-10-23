from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Request
from .models import Answer
from .models import UserAccount


class UserAccountResource(resources.ModelResource):
    class Meta:
        model = UserAccount


class UserAccountAdmin(ImportExportModelAdmin):
    resource_classes = [UserAccountResource]


admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Request)
admin.site.register(Answer)
