from django.urls import path
from .views import UserAPIView, AccountAPIView


urlpatterns = [
    path('user/', UserAPIView.as_view(), name='user'),
    path('account/', AccountAPIView.as_view(), name='account'),
]