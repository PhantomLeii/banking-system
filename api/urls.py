from django.urls import path
from .views import (
    UserAPIView,
    AccountAPIView,
    login_view,
    signup_view,
    logout_view,
    deposit_view,
    AccountDetailAPIView,
    withdraw_view
)


urlpatterns = [
    # User related endpoints
    path('user/', UserAPIView.as_view(), name='user'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', signup_view, name='register'),

    # Account related endpoints
    path('accounts/', AccountAPIView.as_view(), name='accounts'),
    path('account/delete/<int:pk>/', AccountAPIView.as_view(), name='del-account'),
    path('deposit/<int:pk>/', deposit_view, name='deposit'),
    path('account/detail/<int:pk>/', AccountDetailAPIView.as_view(), name='account-detail'),
    path('withdraw/<int:pk>/', withdraw_view, name='withdraw'),
]