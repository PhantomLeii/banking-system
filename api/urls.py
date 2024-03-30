from django.urls import path
from .views import UserAPIView, login_view


urlpatterns = [
    path('user/', UserAPIView.as_view(), name='user'),
    path('login/', login_view, name='login'),
]