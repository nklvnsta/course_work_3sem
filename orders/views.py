from django.contrib.auth import get_user_model
from rest_framework import  viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated

from .models import Order
from .pagination import SmallPagesPagination
from .serializers import OrderSerializer
from .filters import IsOwnerFilterBackend



class OrdersViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = SmallPagesPagination
    permission_classes = [IsAuthenticated]
    # фильтр по пользователям
    filter_backends = [IsOwnerFilterBackend]
   