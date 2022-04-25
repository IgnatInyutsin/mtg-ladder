from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls
from restapi.app.views import ActivationViewSet, UserListViewSet

urlpatterns = []

urlpatterns += doc_urls

urlpatterns += [
    path(r'api/auth/users/', UserListViewSet.as_view({"get": "list"})),
    path(r'api/auth/users/activate/<str:uid>/<str:token>/', ActivationViewSet.as_view({"get": "list"})),
    path(r'api/auth/admin/', admin.site.urls),
    path('api/auth/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/auth/', include('djoser.urls.jwt')),
]