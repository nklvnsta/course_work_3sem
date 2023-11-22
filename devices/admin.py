from django.contrib import admin

from devices.models import Device, SparePart

from simple_history.admin import SimpleHistoryAdmin

from import_export.admin import ImportExportMixin,ExportActionModelAdmin


@admin.register(Device)
class DeviceAdmin(ImportExportMixin,ExportActionModelAdmin,SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'serial_number')
    list_filter = ('name', 'model', 'serial_number')
    search_fields = ('id', 'name', 'model', 'serial_number')
    list_display_links = ('id', 'name', 'model', 'serial_number')
    filter_horizontal = ('spare_parts',)


@admin.register(SparePart)
class SparePartAdmin(SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'delivery_time',)
    list_filter = ('id', 'name', 'price', 'delivery_time',)
    search_fields = ('id', 'name', 'price', 'delivery_time',)
    list_display_links = ('id', 'name', )
    list_editable = ('price', 'delivery_time',)

