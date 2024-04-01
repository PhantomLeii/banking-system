from django.urls import path
from .views import UserAPIView, login_view, signup_view, logout_view


urlpatterns = [
    path('user/', UserAPIView.as_view(), name='user'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', signup_view, name='register'),
]