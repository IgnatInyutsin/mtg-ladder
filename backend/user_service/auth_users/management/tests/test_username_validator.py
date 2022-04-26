from rest_framework.test import APITestCase
from restapi.app.serializers import RegistrationSerializer
from django.contrib.auth.models import User
from rest_framework.serializers import ValidationError

class UsernameValidatorTest(APITestCase):
    def setUp(self):
        # создаем пользователя
        User(username="test", password="test").save()
    def test_access_working(self):
        # проверка на работу без ошибки
        self.assertEqual(RegistrationSerializer.validate_username(None, "testing"), "testing")
    def test_unique_option(self):
        try:
            # если не вызвало ошибок - тест не пройден
            self.assertEqual(RegistrationSerializer.validate_username(None, "test"), not "test")
        except ValidationError as error:
            self.assertEqual(str(error), "[ErrorDetail(string='A User with this name already exists.', code='invalid')]")