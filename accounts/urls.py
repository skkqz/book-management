from django.urls import path
from .views import UserListView, UserRegisterAPIView


urlpatterns = [
    path('user/all/', UserListView.as_view(), name='user-all'),
    path('user/registration/', UserRegisterAPIView.as_view(), name='user-registration'),
]
