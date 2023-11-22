from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users.models import CustomerProfile, StaffProfile

from import_export.admin import ImportExportMixin,ExportActionModelAdmin

User = get_user_model()


class CustomerProfileInlined(admin.StackedInline):
    model = CustomerProfile
    can_delete = False


class StaffProfileInlined(admin.StackedInline):
    model = StaffProfile
    can_delete = False


class UserAdmin(ImportExportMixin,ExportActionModelAdmin,UserAdmin):
    inlines = (CustomerProfileInlined, StaffProfileInlined, )
    list_display = ('username', 'get_full_name', 'email', 'is_staff',)
    list_display_links = ('username', 'get_full_name', 'email',)
    list_filter = ('is_staff',)

    @admin.display(description='ФИО пользователя')
    def get_full_name(self, obj):
        return f"{obj.last_name} {obj.first_name} {obj.customer_profile.patronymic}"


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
