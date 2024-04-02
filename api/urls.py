from django.urls import path
from .views import (
    UserAPIView,
    AccountAPIView,
    login_view,
    signup_view,
    logout_view,
    deposit_view,
)


urlpatterns = [
    # User related endpoints
    path('user/', UserAPIView.as_view(), name='user'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', signup_view, name='register'),

    # Account related endpoints
    path('accounts/', AccountAPIView.as_view(), name='accounts'),
    path('accounts/<int:pk>/', AccountAPIView.as_view(), name='del-account'),
    path('deposit/<int:pk>/', deposit_view, name='deposit'),
]