from rest_framework import viewsets
from restapi.app.cards.serializers import CardSerializer
from  restapi.app.cards.models import Card

#класс для запросов на админа, доступен только get
class CardsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Card.objects.all().order_by('id')
    serializer_class = CardSerializer