from django.contrib import admin

from orders.models import Order

from simple_history.admin import SimpleHistoryAdmin

from import_export.admin import ImportExportMixin,ExportActionModelAdmin

@admin.register(Order)
class OrderAdmin(ImportExportMixin,ExportActionModelAdmin,SimpleHistoryAdmin,admin.ModelAdmin):
    @admin.display(description='ФИО заказчика')
    def full_name(self, obj):
        return f"{obj.customer.first_name} {obj.customer.last_name} {obj.customer.customer_profile.patronymic}"

    list_display = ('id', 'full_name', 'price', 'status', 'created_at')
    list_display_links = ('id', 'full_name')
    list_filter = ('status', 'created_at')
    search_fields = ('id', 'customer__username', 'customer__email')
    raw_id_fields = ('customer',)
    date_hierarchy = 'created_at'