from rest_framework import serializers
from restapi.app.cards.rules.models import CardRule

class CardRuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardRule
        fields = ["id", "date", "text"]