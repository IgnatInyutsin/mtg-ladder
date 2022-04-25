from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls

urlpatterns = []

urlpatterns += doc_urls

urlpatterns += [
    path('api/cards/admin/', admin.site.urls),
    path('api/cards/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/cards/', include('restapi.app.routes')),
]