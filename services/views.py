from django.contrib.auth import get_user_model
from rest_framework import  viewsets
from rest_framework.permissions import AllowAny

from .models import Service
from .pagination import SmallPagesPagination
from .serializers import ServiceSerializer



class ServicesViewSet(viewsets.ModelViewSet):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = SmallPagesPagination
    permission_classes = [AllowAny, ]