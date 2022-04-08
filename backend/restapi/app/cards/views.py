from rest_framework import viewsets
from restapi.app.cards.serializers import CardSerializer
from  restapi.app.cards.models import Card
from django.db.models import Q

#класс для запросов на админа, доступен только get
class CardsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Card.objects.all().order_by('id')
    serializer_class = CardSerializer

    def get_queryset(self):
        queryset = self.queryset
        # фильтр по имени
        if "name" in self.request.query_params:
            queryset = queryset.filter(name__icontains=self.request.query_params.get("name"))
        # фильтр по тексту
        if "text" in self.request.query_params:
            queryset = queryset.filter(text__icontains=self.request.query_params.get("text"))
        # фильтр по минимальной мана-стоимости
        if "mana_value_min" in self.request.query_params:
            try:
                queryset = queryset.filter(mana_value__gte=int(self.request.query_params.get("mana_value_min")))
            except: pass
        # фильтр по максимальной мана-стоимости
        if "mana_value_max" in self.request.query_params:
            try:
                queryset = queryset.filter(mana_value__lte=int(self.request.query_params.get("mana_value_max")))
            except: pass
        # фильтр по цвету
        if "colors" in self.request.query_params:
            colors = self.request.query_params.getlist("colors", "")
            for i in range(len(colors)):
                queryset = queryset.filter(colors__icontains=colors[i])
        # фильтр по типу
        if "types" in self.request.query_params:
            types = self.request.query_params.getlist("types", "")
            for i in range(len(types)):
                queryset = queryset.filter(types__icontains=types[i])

        return queryset