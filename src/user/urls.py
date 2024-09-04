from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from user.views import UserCreateView,UserLoginView,UserLogoutView,UserChangePasswordView,UserForgotPassword


urlpatterns = [
    
   
    path('create/',UserCreateView.as_view()),
    path('login/',UserLoginView.as_view()),
    path('logout/',UserLogoutView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('changepassword/',UserChangePasswordView.as_view()),
    path('forgotpassword/',UserForgotPassword.as_view()),

]
