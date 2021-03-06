from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Инициализация автодокументирования

schema_view = get_schema_view(
    openapi.Info(
        title="MTG Ladder USER Service API",
        default_version='v1',
        description='Сервис для взаимодействия с пользователями MTG Ladder',
        license=openapi.License(name='BSD License')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('api/auth_users/documentation(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/auth_users/documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]