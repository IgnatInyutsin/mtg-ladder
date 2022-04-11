from rest_framework import viewsets, mixins
from restapi.app.cards.rules.serializers import CardRuleSerializer
from restapi.app.cards.rules.models import CardRule
from restapi.app.cards.models import Card
from django.http import Http404

#класс для запросов на админа, доступен только get
class CardRuleViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = CardRule.objects.all().order_by('id')
    serializer_class = CardRuleSerializer
    pagination_class = None

    def get_queryset(self):
        cardId = self.kwargs["cardId"]

        # проверяем на наличие карты
        if not Card.objects.all().filter(id=cardId).exists():
            raise Http404

        return CardRule.objects.all().filter(
            card=Card.objects.get(id=int(cardId))
        )