from requests import JSONDecodeError
from rest_framework import viewsets
from rest_framework import mixins
from restapi.app.serializers import UserSerializer
from django.contrib.auth.models import User
import requests
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

# метод get для пользователей
class UserListViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = User.objects.all().filter(is_active=True).order_by('id')
    serializer_class = UserSerializer

    @swagger_auto_schema(operation_description="Список всех пользователей")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

# метод подтверждения регистрации по get
class ActivationViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    @swagger_auto_schema(operation_description="Запрос активации аккаунта",
                        responses={200: "{detail: \"detail text\"}"})
    def list(self, request, token, uid):
        # автоматическое изменение протокола
        protocol = 'https://' if request.is_secure() else 'http://'
        # добавление основной части ссылки
        web_url = protocol + request.get_host() + ":8000"
        # добавление пути
        post_url = web_url + "/api/auth/users/activation/"
        # отправка запроса на активацию
        post_data = {'uid': uid, 'token': token}
        result = requests.post(post_url, data=post_data)
        # если ошибка 500 - заполняем сообщением об ошибке, иначе - тело сообщения
        content = {"detail": "Server error. Please, check spam directory."} if str(result.status_code)[0] == 5 else result.json()
        # возвращаем ответ
        return Response(content)