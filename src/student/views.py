from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .utils import get_tokens_for_user # type: ignore
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializer import forgotpasswordSerializer


class UserCreateView(APIView):
    def post(self, request):
        data = request.data
        try:
            username = data["username"]
            email = data["email"]
            password = data["password"]
        except KeyError as key:
            return Response(
                {str(key): ["field required"]}, status=status.HTTP_400_BAD_REQUEST
            )
        if User.objects.filter(username=username).exists():
            return Response(
                {"username": ["this user already exists"]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = User.objects.create(email=email, username=username)
        user.set_password(password)
        user.save()
        res = {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
        return Response(
            {"message": "user created", "user": res}, status=status.HTTP_201_CREATED
        )


class UserLoginView(APIView):
    def post(self, request):
        data = request.data
        User_name = request.data["username"]
        password = data["password"]
        try:
            user = User.objects.get(username=User_name)
        except user.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        if authenticate(username=User_name, password=password):
            token = get_tokens_for_user(user)
            return Response({"token": token}, status=200)
        else:
            return Response(
                {"message": "Invalid Credientials"}, status=status.HTTP_401_UNAUTHORIZED
            )


class UserLogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        try:
            Token.objects.get(user=request.user)
            Token.delete()
            return Response({"message": "user logout"}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response(
                {"message": "user already logout"}, status=status.HTTP_404_NOT_FOUND
            )


class UserChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        data = request.data
        current_password = data['current_password']
        new_password = data['new_password']
        conform_password = data['conform_password']
        if authenticate(username = request.user.username,password=current_password):
            if new_password == conform_password:
                    request.user.set_password(new_password)
                    request.user.save()
                    return Response({"message":"password changed"},status=status.HTTP_200_OK)
            else:
                    return Response({"message":"password not match"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"invalid password "},status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        data = request.data
        current_password = data["current_password"]
        new_password = data["new_password"]
        conform_password = data["conform_password"]
        if authenticate(username=request.user.username, password=current_password):
            if new_password == conform_password:
                request.user.set_password(new_password)
                request.user.save()
                return Response(
                    {"message": "password changed"}, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"message": "password not match"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {"message": "invalid password "}, status=status.HTTP_400_BAD_REQUEST
            )


class UserForgotPassword(APIView):
    serializer_class = forgotpasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            user = User.objects.filter(email=email).first()
            if user:
                return Response({"message": "Password reset email sent."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
