from rest_framework import status
from rest_framework.generics import UpdateAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from users.models import User
from users.permissions import IsCurrentUser
from users.serializers import UserSerializer, UserRegistrationSerializer


class UserRegistrationView(CreateAPIView):
    """Регистрация пользователя"""

    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class UserListView(ListAPIView):
    """Отображение списка пользователей"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserCreateView(CreateAPIView):
    """Создание нового пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDetailView(RetrieveAPIView):
    """Отображение одного пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserUpdateView(UpdateAPIView):
    """Изменение пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsCurrentUser]


class UserDeleteView(DestroyAPIView):
    """Удаление пользователя"""
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsCurrentUser]
