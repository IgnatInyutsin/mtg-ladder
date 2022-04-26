from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls

urlpatterns = []

urlpatterns += doc_urls

urlpatterns += [
    path(r'api/auth_users/users/', include('auth_users.app.routes')),
    path(r'api/auth_users/admin/', admin.site.urls),
    path('api/auth_users/api-auth_users/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth_users/', include('djoser.urls')),
    path('api/auth_users/', include('djoser.urls.authtoken')),
    path('api/auth_users/', include('djoser.urls.jwt')),
]