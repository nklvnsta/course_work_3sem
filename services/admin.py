from django.contrib import admin

from services.models import Service

from simple_history.admin import SimpleHistoryAdmin

from import_export.admin import ImportExportMixin,ExportActionModelAdmin


@admin.register(Service)
class ServiceAdmin(ImportExportMixin,ExportActionModelAdmin,SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ('id', 'name', 'price', )
    list_filter = ('id', 'name', 'price', )
    search_fields = ('id', 'name', 'price', )
    list_display_links = ('id', 'name', )
    list_editable = ('price', )
