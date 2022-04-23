from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins
from restapi.app.rules.serializers import CardRuleSerializer
from restapi.app.rules.models import CardRule
from restapi.app.models import Card
from django.http import Http404

#класс для запросов на админа, доступен только get
class CardRuleViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = CardRule.objects.all().order_by('id')
    serializer_class = CardRuleSerializer
    pagination_class = None

    def get_queryset(self):
        cardId = self.kwargs["id"]

        # проверяем на наличие карты
        if not Card.objects.all().filter(id=cardId).exists():
            raise Http404

        return CardRule.objects.all().filter(
            card=Card.objects.get(id=int(cardId))
        )

    @swagger_auto_schema(operation_description="Получить список всех правил для данной карты",
                         tags=["card"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)