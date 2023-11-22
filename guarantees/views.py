from django.contrib.auth import get_user_model
from rest_framework import  viewsets
from rest_framework.permissions import AllowAny

from .models import Guarantee
from .pagination import SmallPagesPagination
from .serializers import GuaranteesSerializer

from rest_framework import filters
from rest_framework.decorators import action


class GuaranteeViewSet(viewsets.ModelViewSet):

    queryset = Guarantee.objects.select_related('device').all()
    serializer_class = GuaranteesSerializer
    pagination_class = SmallPagesPagination
    permission_classes = [AllowAny, ]

    
    filterset_fields = ( 'status',)

    
