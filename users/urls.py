from django.urls import path
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserLogoutView,
)

urlpatterns = [
    path("auth/sign-up/", UserRegistrationView.as_view()),
    path("auth/login/", UserLoginView.as_view()),
    path("auth/logout/", UserLogoutView.as_view()),
]
