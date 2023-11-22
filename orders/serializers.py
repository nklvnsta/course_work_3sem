from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Order


User = get_user_model()




class OrderSerializer(serializers.ModelSerializer):

    customer = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='username')
    
    class Meta:
        model = Order
        fields = (
            "id",
            "status",
            "customer",
            "price",
            "created_at",
        )
