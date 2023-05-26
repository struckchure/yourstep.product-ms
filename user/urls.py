from django.urls import path

from user.api import UserLoginAPI, UserRegisterAPI

app_name = "user"

urlpatterns = [
    path("register/", UserRegisterAPI.as_view(), name="register_api"),
    path("login/", UserLoginAPI.as_view(), name="login_api"),
]
