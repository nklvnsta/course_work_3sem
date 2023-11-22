from django.contrib.auth import get_user_model
from rest_framework import  viewsets,filters
from rest_framework.permissions import AllowAny

from .models import Device, SparePart
from .pagination import SmallPagesPagination
from .serializers import DeviceSerializer,SparePartSerializer
from rest_framework.decorators import action
from django.db.models import Q
from rest_framework.response import Response
from datetime import date

class DeviceViewSet(viewsets.ModelViewSet):

    queryset = Device.objects.prefetch_related('spare_parts').all()
    serializer_class = DeviceSerializer
    pagination_class = SmallPagesPagination
    permission_classes = [AllowAny, ]

    @action(methods=['GET'], detail=False)
    def get_phones_headphones(self, request, **kwargs):
        
        queryset = self.get_queryset().filter((~Q(warranty_expiration_date__lt=date.today()) & Q(name__icontains="Смартфон") | Q(name__icontains="Наушники")))
        serializer = DeviceSerializer(queryset,many=True)
        data = dict()
        data['data'] = serializer.data
        return Response(data)

class SpareViewSet(viewsets.ModelViewSet):

    queryset = SparePart.objects.all()
    serializer_class = SparePartSerializer
    pagination_class = SmallPagesPagination
    permission_classes = [AllowAny, ]

    filter_backends = [filters.SearchFilter]
    search_fields = ['delivery_time']

    