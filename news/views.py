from django.contrib.auth import get_user_model
from rest_framework import  viewsets
from rest_framework.permissions import AllowAny

from .models import News
from .pagination import SmallPagesPagination
from .serializers import NewsSerializer



class NewsViewSet(viewsets.ModelViewSet):

    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = SmallPagesPagination
    permission_classes = [AllowAny, ]
