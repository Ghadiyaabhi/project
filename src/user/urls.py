from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import (
    UserCreateView,
    UserLoginView,
    UserLogoutView,
    UserChangePasswordView,
    UserForgotPasswordView,
)

urlpatterns = [
    path("create", UserCreateView.as_view()),
    path("login", UserLoginView.as_view()),
    path("logout", UserLogoutView.as_view()),
    path("change-password", UserChangePasswordView.as_view()),
    path("forgot", UserForgotPasswordView.as_view()),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
