from rest_framework.test import APITestCase
from rest_framework import status
from restapi.management.commands.load_card_database import Command

class SearchCardTest(APITestCase):
    def setUp(self):
        Command.handle(None)
    def test_search(self):
        # тест поиска по имени
        request = self.client.get("/api/cards/?name=Кошка")
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.data.get("results")[0].get("name"), "Черная Кошка")
        # тест поиска по тексту
        request = self.client.get("/api/cards/?text=Подбросьте%20монетку")
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.data.get("results")[0].get("name"), "Гоблин-Бабашник")
        # тест поиска по мана-стоимости
        request = self.client.get("/api/cards/?mana_value_min=13&mana_value_max=13")
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.data.get("results")[0].get("name"), "Эмракул, Обетованная Гибель")
        # тест поиска по цвету
        request = self.client.get("/api/cards/?colors=b&colors=w")
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.data.get("results")[0].get("name"), "Возвышение Абзана")
        # тест поиска по типу
        request = self.client.get("/api/cards/?types=Artifact&types=Creature")
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.data.get("results")[0].get("name"), "Совершенный Автомат")