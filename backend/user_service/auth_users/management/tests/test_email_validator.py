from rest_framework.test import APITestCase
from restapi.app.serializers import RegistrationSerializer
from django.contrib.auth.models import User
from rest_framework.serializers import ValidationError

class EmailValidatorTest(APITestCase):
    def setUp(self):
        # создаем пользователя
        User(username="test", password="test", email="test@test.com").save()
    def test_access_working(self):
        # проверка на работу без ошибки
        self.assertEqual(RegistrationSerializer.validate_email(None, "testing@test.com"), "testing@test.com")
    def test_unique_option(self):
        try:
            # если не вызвало ошибок - тест не пройден
            self.assertEqual(RegistrationSerializer.validate_email(None, "test@test.com"), not "test@test.com")
        except ValidationError as error:
            self.assertEqual(str(error), "[ErrorDetail(string='A User with this email already exists.', code='invalid')]")
    def test_format_option(self):
        try:
            # если не вызвало ошибок - тест не пройден
            self.assertEqual(RegistrationSerializer.validate_email(None, "test"), not "test")
        except ValidationError as error:
            self.assertEqual(str(error), "[ErrorDetail(string='A email format is wrong.', code='invalid')]")