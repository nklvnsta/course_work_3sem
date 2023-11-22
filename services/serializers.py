from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Service

User = get_user_model()




class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = (
            "id",
            "name",
            "price",
        )
