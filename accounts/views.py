from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import UserSerializer, UserRegisterSerializer
from .tasks import send_welcome_email


class UserListView(generics.ListAPIView):
    """
    Список пользователей
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserRegisterAPIView(generics.CreateAPIView):

    """
    Представление для регистрации пользователя.
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        print('[INFO]: ОБРАБОТКА ЗАДАЧИ CELERY')
        user = serializer.save()
        send_welcome_email.delay(user.email)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
