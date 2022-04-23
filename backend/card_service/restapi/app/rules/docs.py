from drf_yasg import openapi
from rest_framework import serializers

class CardRuleDateField(serializers.DateField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "title": "CardRuleDate",
            "description": "Дата принятия правила в ISO8601"
        }

class CardRuleTextField(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "title": "CardRuleText",
            "description": "Текст правила"
        }