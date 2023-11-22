from django.contrib import admin

from devices.models import Device

from .models import Guarantee

from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportMixin,ExportActionModelAdmin


from import_export import resources, fields,widgets
from django.db.models import Q

from import_export.widgets import ForeignKeyWidget



class GuaranteeResource(resources.ModelResource):
    
    item_status = fields.Field(attribute='item_status', column_name='Статус')
    device = fields.Field(
       attribute="device",
       column_name="Устройство",
       widget=ForeignKeyWidget(Device, "name")
   )
     
    class Meta:
        model = Guarantee
       
        fields = ('id', 'device', 'datetime_started', 'datetime_finished', 'item_status',)
        export_order = fields

    def dehydrate_item_status(self, guarantee):
        val =  guarantee.status
        def F(value,choices):
            for i in choices:
                if val == i[0]:
                    return i[1]
        res = F(val,(
        (0, "Активна"),
        (1, "Просрочена"),
        (2, "Использована"),
        ))
        return res
    
    def get_export_headers(self):
        headers = []
        for field in self.get_fields():
            model_fields = self.Meta.model._meta.get_fields()
            header = next((x.verbose_name for x in model_fields if x.name == field.column_name), field.column_name)
            headers.append(header)
        return headers
 
    
   

@admin.register(Guarantee)
class GuaranteeAdmin(ImportExportMixin,ExportActionModelAdmin,SimpleHistoryAdmin,admin.ModelAdmin):

    @admin.display(description="Устройство")
    def device_name_and_model(self, obj):
        return f"{obj.device.name} {obj.device.model}"

    list_display = ('id', 'device_name_and_model', 'datetime_started', 'datetime_finished', 'status',)
    list_display_links = ('id', 'device_name_and_model', 'datetime_started', 'datetime_finished', 'status',)
    search_fields = ('id', 'datetime_started', 'datetime_finished', 'status',)
    raw_id_fields = ('device',)

    date_hierarchy = 'datetime_started'

    resource_class = GuaranteeResource

    def get_export_queryset(self, request):
        return Guarantee.objects.filter(~Q(status=1) & (Q(status=0) | Q(status=2)))