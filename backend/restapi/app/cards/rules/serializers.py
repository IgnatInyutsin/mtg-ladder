from restapi.app.cards.rules.models import CardRule
from .docs import *

class CardRuleSerializer(serializers.HyperlinkedModelSerializer):
    date = CardRuleDateField()
    text = CardRuleTextField()
    class Meta:
        model = CardRule
        fields = ["id", "date", "text"]