from rest_framework import viewsets
from rest_framework import mixins
from auth_users.app.serializers import UserSerializer, RegistrationSerializer
from django.contrib.auth.models import User
import requests
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

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
        post_url = web_url + "/api/auth_users/users/activation/"
        # отправка запроса на активацию
        post_data = {'uid': uid, 'token': token}
        result = requests.post(post_url, data=post_data)
        # если ошибка - заполняем сообщением об ошибке, иначе - тело сообщения
        try:
            content = result.json()
            # возвращаем ответ
            return Response(content)
        except:
            return Response({"detail": "Please, check spam directory"}, status=400)