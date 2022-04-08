from django.urls import include, path
from rest_framework import routers
from restapi.app.cards.views import CardsViewSet

#устанавливаем пути
router = routers.DefaultRouter()
router.register('', CardsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]