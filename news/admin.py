from django.contrib import admin

from news.models import News

from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportMixin,ExportActionModelAdmin

@admin.register(News)
class NewsAdmin(ImportExportMixin,ExportActionModelAdmin,SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ("id",
                    "title",
                    "datetime_updated",
                    "datetime_created",
                    )
    list_display_links = ("id",
                          "title",
                          )
    search_fields = (
        "id",
        "title",
    )
    list_filter = (
        "datetime_created",
    )
    date_hierarchy = "datetime_created"
