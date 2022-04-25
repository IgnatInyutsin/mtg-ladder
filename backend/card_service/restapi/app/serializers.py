from restapi.app.models import *
from .docs import *
from rest_framework import serializers

# Сериализатор для GET
class CardSerializer(serializers.HyperlinkedModelSerializer):
    scryfall_id = ScryfallIdField()
    name = CardNameField()
    text = CardTextField()
    colors = ColorsField()
    types = TypesField()
    mana_value = ManaValueField()
    mana_cost = ManaCostField()
    power = PowerField()
    toughness = ToughnessField()
    loyalty = LoyaltyField()

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