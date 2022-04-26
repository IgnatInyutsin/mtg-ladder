from django.urls import include, path
from rest_framework import routers
from .views import ActivationViewSet

#устанавливаем пути
router = routers.DefaultRouter()
router.register("activate/(?P<uid>[\w.@+-]+)/(?P<token>[\w.@+-]+)", ActivationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]