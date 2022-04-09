from rest_framework import serializers
from restapi.app.cards.models import *

class CardRuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardRule
        fields = ["id", "date", "text"]

# Сериализатор для GET
class CardSerializer(serializers.HyperlinkedModelSerializer):
    rules = CardRuleSerializer(many=True)
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
                  'loyalty',

                  'rules']