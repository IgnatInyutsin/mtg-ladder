from django.core.management.base import BaseCommand
from restapi.app.models import *
from restapi.app.rules.models import *
import requests
import json
from django.db import transaction
from datetime import datetime

class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        print("Loading cards...")

        # удаляем все карты, которые были в таблице раньше
        Card.objects.all().delete()

        # собираем данные о картах
        response = json.loads(requests.get('https://mtgjson.com/api/v5/PioneerAtomic.json').text).get("data")


        # перебираем все карты
        for card in response:
            english_name = card
            english_text = response.get("text", None)
            # подбираем русский язык
            for localy in response[card][0].get("foreignData", []):
                if localy.get("language") == "Russian":
                    # забираем имя и текст
                    name = localy.get("name")
                    text = localy.get("text", None)
                    break
            else:
                # если нет русского - делаем названия на английском
                name = response[card][0].get("name")
                text = response[card][0].get("text", None)

            # сохраняем в базу данных карту
            card_orm = Card(
                name=name,
                mana_value=response[card][0].get("manaValue", None),
                mana_cost=response[card][0].get("manaCost", None),
                colors=response[card][0].get("colors", None),
                text=text,
                types=response[card][0].get("types"),
                power=response[card][0].get("power", None),
                toughness=response[card][0].get("toughness", None),
                loyalty=response[card][0].get("loyalty", None),
                scryfall_id=response[card][0].get("identifiers").get("scryfallOracleId"),
                english_name=english_name,
                english_text=english_text,
            )
            card_orm.save()

            # если есть правило - добавляем
            for rule in response[card][0].get("rulings", []):
                card_rule = CardRule(
                    date=datetime.strptime(rule.get("date"), '%Y-%m-%d'),
                    text=rule.get("text"),
                    card=card_orm
                )
                card_rule.save()

            print(name + " is pulling in database!")



        print('Loading finished!')
        return "End."