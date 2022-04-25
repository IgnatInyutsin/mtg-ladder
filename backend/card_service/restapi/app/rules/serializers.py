from restapi.app.rules.models import CardRule
from .docs import *
from rest_framework import serializers

class CardRuleSerializer(serializers.HyperlinkedModelSerializer):
    date = CardRuleDateField()
    text = CardRuleTextField()
    class Meta:
        model = CardRule
        fields = ["id", "date", "text"]