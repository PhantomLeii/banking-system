from django.urls import path
from .views import CreateAccountView, UserAccountsView, AccountDetailView


urlpatterns = [
    path("", UserAccountsView.as_view()),
    path("create/", CreateAccountView.as_view()),
    path("<int:pk>/detail/", AccountDetailView.as_view()),
]
