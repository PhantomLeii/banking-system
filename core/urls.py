from django.urls import path
from .views import (
    HomePageView,
    LoginView,
    LogoutView,
    RegisterView,
    AccountsView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/',RegisterView.as_view(), name='register'),
    path('accounts/', AccountsView.as_view(), name='accounts'),
]
