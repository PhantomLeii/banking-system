from django.urls import path
from .views import (
    HomePageView,
    LoginView,
    LogoutView,
    RegisterView,
    AccountsView,
    CreateAccountView,
    AccountDetailView,
    DeleteAccountView,
    not_found,
    index,
)

urlpatterns = [
    path('', index, name='index'),
    path('home/', HomePageView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/',RegisterView.as_view(), name='register'),
    path('accounts/', AccountsView.as_view(), name='accounts'),
    path('create-account/', CreateAccountView.as_view(), name='create-account'),
    path('account-detail/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('delete-account/<int:pk>/', DeleteAccountView.as_view(), name='delete-account-form'),
    path('delete-account/<int:pk>/', DeleteAccountView.as_view(), name='delete-account'),
    path('not-found/', not_found, name='not-found'),
]
