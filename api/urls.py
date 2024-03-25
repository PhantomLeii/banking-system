from django.urls import path, include
from . import views


urlpatterns = [
    path('token-auth/', views.ObtainJWTToken, name='api-token-auth'),
    path('user/', views.UserAPView, name='user'),
]