from rest_framework import serializers



from .models import Guarantee

from devices.models import Device

class GuaranteesSerializer(serializers.ModelSerializer):

    device = serializers.SlugRelatedField(queryset=Device.objects.all(),slug_field='name')
   
    datetime_started = serializers.DateTimeField()
    datetime_finished = serializers.DateTimeField()
    status = serializers.ChoiceField(choices=(
        (0, "Активна"),
        (1, "Просрочена"),
        (2, "Использована"),
    ))
   
   
    class Meta:
        model = Guarantee
       
        fields = [
            'id',
            'device',
			'datetime_started',
            'datetime_finished',
            'status',
		] 

