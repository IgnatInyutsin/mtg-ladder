from django.test import TestCase
from restapi.management.commands.load_card_database import Command
from restapi.app.cards.models import *

class LoadCardDatabaseTest(TestCase):
    def test_creating_cards(self):
        # Проверяем, что выполнился без ошибок
        self.assertEqual(Command.handle(None), True)
        # Проверяем количество карт
        self.assertEqual(len(Card.objects.all()) > 8900, True)
        # Проверяем количество правил
        self.assertEqual(len( CardRule.objects.all() ) > 15000, True)