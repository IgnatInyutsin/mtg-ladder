from rest_framework import viewsets
from restapi.app.serializers import CardSerializer
from restapi.app.models import Card
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from .docs import *

#класс для запросов на админа, доступен только get
class CardsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Card.objects.all().order_by("name")
    serializer_class = CardSerializer

    def get_queryset(self):
        queryset = self.queryset
        # фильтр по имени
        if "name" in self.request.query_params:
            queryset = queryset.filter(Q(name__icontains=self.request.query_params.get("name")) |
                                       Q(english_name__icontains=self.request.query_params.get("name")))
        # фильтр по тексту
        if "text" in self.request.query_params:
            queryset = queryset.filter(Q(text__icontains=self.request.query_params.get("text")) |
                                       Q(english_text__icontains=self.request.query_params.get("text")))
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

    @swagger_auto_schema(operation_description="Получить список всех карт",
        tags=["card"],
        manual_parameters=[
            name_query_param,
            text_query_param,
            mana_value_max_query_param,
            mana_value_min_query_param,
            types_query_param,
            colors_query_param])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Получить конкретную карту по ID",
                         tags=["card"])
    def retrieve(self, request, pk):
        return super(CardsViewSet, self).retrieve(request, pk)