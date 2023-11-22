from rest_framework import serializers


from .models import Device, SparePart

from rest_framework.validators import UniqueTogetherValidator,ValidationError

from datetime import datetime

class DeviceSerializer(serializers.ModelSerializer):

    spare_parts = serializers.SlugRelatedField(
        many=True,
        queryset = SparePart.objects.all(),
        read_only=False,
        slug_field='name'
     )

    purchase_date = serializers.DateField()
    warranty_expiration_date = serializers.DateField()

    class Meta:
        model = Device

        fields = [
            'id',
            'name',
			'model',
            'purchase_date',
            'warranty_expiration_date',
            'serial_number',
            'spare_parts',
		] 

        validators = [
            UniqueTogetherValidator(
                queryset=Device.objects.all(),
                fields=['serial_number'],
                message='Серийный номер должен быть уникальным!'
            )
        ]
    
    def validate_name(self, name):
        if len(name) < 10:
            raise ValidationError('Минимальная длина имени устройства 10 символов')
        return name
    
    def validate_model(self, model):
        if len(model) < 15:
            raise ValidationError('Минимальная длина названия модели 15 символов')
        return model
    def validate_serial_number(self,serial_number):
        if len(serial_number) < 8:
            raise ValidationError('Минимальная длина серийного номера 8 символов')
        return serial_number
    def validate_purchase_date(self, purchase_date):
        dat1 = purchase_date
        
        dat2 = datetime.date(datetime.strptime(dict(self.initial_data)['warranty_expiration_date'][0],'%Y-%m-%d')) 
        print(dat1)
        print(dat2) 
        if dat1 > dat2:
            raise ValidationError('Дата окончания гарантии не может истечь раньше даты покупки')

        return purchase_date
    
    

class SparePartSerializer(serializers.ModelSerializer):

    class Meta:
        model = SparePart
       
        fields = [
            'id',
            'name',
			'price',
            'delivery_time',
		] 