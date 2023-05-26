from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import NotAuthenticated

from user.serializers import LoginUserSerializer, RegisterUserSerializer


class UserService:
    @staticmethod
    def register_user(register_user_data):
        register_user_serializer = RegisterUserSerializer(data=register_user_data)
        register_user_serializer.is_valid(raise_exception=True)
        register_user_serializer.save()

        return register_user_serializer.data

    @staticmethod
    def login_user(login_user_data):
        login_user_serializer = LoginUserSerializer(data=login_user_data)
        login_user_serializer.is_valid(raise_exception=True)

        username = login_user_serializer.data["username"]
        password = login_user_serializer.data["password"]

        user = authenticate(username=username, password=password)

        if not user:
            raise NotAuthenticated("Invalid username or password")

        token, _ = Token.objects.get_or_create(user=user)

        return {"token": token.key}
