from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from user.service import UserService


class UserRegisterAPI(GenericAPIView):
    def post(self, request):
        return Response(
            UserService.register_user(request.data),
            status=status.HTTP_201_CREATED,
        )


class UserLoginAPI(GenericAPIView):
    def post(self, request):
        return Response(UserService.login_user(request.data))
