from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from devices.views import DeviceViewSet,SpareViewSet
from guarantees.views import GuaranteeViewSet
from news.views import NewsViewSet
from orders.views import OrdersViewSet
from services.views import ServicesViewSet
from users.views import UsersViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'devices',DeviceViewSet)
router.register(r'spares',SpareViewSet)
router.register(r'guarantee',GuaranteeViewSet)
router.register(r'news',NewsViewSet)
router.register(r'orders',OrdersViewSet)
router.register(r'services',ServicesViewSet)
router.register(r'users',UsersViewSet)
schema_view = get_schema_view(
    openapi.Info(
        title="Service center API",
        default_version="v1",
        description="Service center API",
    ),
    public=True,
    permission_classes=[permissions.IsAdminUser],
)

urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path('api/v1/',include(router.urls)),

    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include(("users.urls", "users"), namespace="users")),
]
