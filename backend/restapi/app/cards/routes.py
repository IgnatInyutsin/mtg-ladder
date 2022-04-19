from django.urls import include, path
from rest_framework import routers
from restapi.app.cards.views import CardsViewSet
from restapi.app.cards.rules.views import CardRuleViewSet

#устанавливаем пути
router = routers.DefaultRouter()
router.register(r'(?P<id>[0-9]+)/rules', CardRuleViewSet)
router.register('', CardsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]