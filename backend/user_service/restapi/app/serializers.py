from rest_framework import serializers
from restapi.app.models import *
from django.contrib.auth.models import User
from email.utils import parseaddr

class PioneerProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PioneerProfile
        fields = ["id", "elo", "max_elo", "min_elo"]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    description = serializers.CharField(source="profile.description")
    pioneer = PioneerProfileSerializer()
    class Meta:
        model = User
        fields = ["id",
                  "username",
                  "first_name",
                  "last_name",
                  "description",
                  "email",
                  "date_joined",
                  "pioneer"]

class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name", "email", "password"]

    def validate_username(self, value):
        # Получаем всех пользователей с этим именем
        check_query = User.objects.filter(username=value)

        # Если есть хотя бы один - ошибка, при регистрации такого быть не должно
        if check_query.exists():
            raise serializers.ValidationError('A User with this name already exists.')
        # Иначе успешно
        return value

    def validate_email(self, value):
        # если email неправильного формата
        if not '@' in parseaddr(value)[1]:
            raise serializers.ValidationError('A email format is wrong.')

        # Получаем всех пользователей с этим email
        check_query = User.objects.filter(email=value)

        # Если есть хотя бы один - ошибка, при регистрации такого быть не должно
        if check_query.exists():
            raise serializers.ValidationError('A User with this email already exists.')

        # Иначе успешно
        return value