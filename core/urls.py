from django.urls import path
from .views import (
    HomePageView,
    LoginView,
    LogoutView,
    RegisterView,
    AccountsView,
    CreateAccountView,
    AccountDetailView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/',RegisterView.as_view(), name='register'),
    path('accounts/', AccountsView.as_view(), name='accounts'),
    path('create-account/', CreateAccountView.as_view(), name='create-account'),
    path('account-detail/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
]
