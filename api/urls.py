from django.urls import path
from .views import UserAPIView, AccountAPIView, CreateUserView


urlpatterns = [
    path('user/', UserAPIView.as_view(), name='user'),
]