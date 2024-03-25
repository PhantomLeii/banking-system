from django.urls import path, include
from . import views


urlpatterns = [
    path('user/', views.UserAPIView.as_view(), name='user'),
]