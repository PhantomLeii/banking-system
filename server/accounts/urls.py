from django.urls import path
from .views import CreateAccountView, AccountsDetailView


urlpatterns = [
    path("", AccountsDetailView.as_view()),
    path("create/", CreateAccountView.as_view()),
]
