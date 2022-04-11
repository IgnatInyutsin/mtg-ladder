from rest_framework import serializers
from restapi.app.cards.models import *

# Сериализатор для GET
class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ['id',
                  'scryfall_id',

                  'name',
                  'text',

                  'colors',
                  'types',

                  'mana_value',
                  'mana_cost',

                  'power',
                  'toughness',
                  'loyalty']