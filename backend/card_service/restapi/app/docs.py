from drf_yasg import openapi
from rest_framework import serializers

# создание полей для сериализатора - для описание swagger
class ScryfallIdField(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "title": "ScryfallOracleId",
            "description": "ScryfallOracleId для взаимодействия с ScryfallAPI"
        }
class CardNameField(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "title": "CardName",
            "description": "Имя карты, приоритетнее - русский"
        }
class CardTextField(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "title": "CardText",
            "description": "Текст карты, приоритетнее - русский"
        }

class ColorsField(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_ARRAY,
            "title": "CardColors",
            "description": "Цвета карты",
            "example": ["W", "U", "B", "R", "G"],
            "items": {"type": openapi.TYPE_STRING}
        }
class TypesField(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_ARRAY,
            "title": "CardTypes",
            "description": "Типы карт",
            "items": {"type": openapi.TYPE_STRING}
        }
class ManaValueField(serializers.IntegerField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_NUMBER,
            "title": "CardManaValue",
            "description": "Числовое значение мана-стоимости"
        }
class ManaCostField(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "title": "CardManaCost",
            "description": "Значение конвертированной мана-стоимости, состоящее из спец-символов"
        }
class PowerField(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "title": "CardPower",
            "description": "Присуствует у существ и машин, обозначает силу существа"
        }
class ToughnessField(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "title": "CardToughness",
            "description": "Присуствует у существ и машин, обозначает выносливость существа"
        }
class LoyaltyField(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "title": "CardLoyalty",
            "description": "Присуствует у мироходцев, обозначает их лояльность"
        }

# описание query_params полей
name_query_param = openapi.Parameter('name',
                                     openapi.IN_QUERY,
                                     description="Поиск по ключевым целым словам в имени - на английском и русском",
                                     type=openapi.TYPE_STRING)
text_query_param = openapi.Parameter('text',
                                     openapi.IN_QUERY,
                                     description="Поиск по ключевым целым словам в тексте - на английском и русском",
                                     type=openapi.TYPE_STRING)
mana_value_min_query_param = openapi.Parameter('mana_value_min',
                                     openapi.IN_QUERY,
                                     description="Поиск по минимальной мана стоимости",
                                     type=openapi.TYPE_NUMBER)
mana_value_max_query_param = openapi.Parameter('mana_value_max',
                                     openapi.IN_QUERY,
                                     description="Поиск по максимальной мана стоимости",
                                     type=openapi.TYPE_NUMBER)
colors_query_param = openapi.Parameter('colors',
                                    openapi.IN_QUERY,
                                    description="Поиск по цветам - цвета в массиве обозначены одной буквой",
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Items(type=openapi.TYPE_STRING))

types_query_param = openapi.Parameter('types',
                                    openapi.IN_QUERY,
                                    description="Поиск по типам, имена типов обязательно должны быть на английском языке",
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Items(type=openapi.TYPE_STRING))