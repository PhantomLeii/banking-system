from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegistrationView,
    UserProfileView,
    UpdateUserView,
    DeleteUserView,
    LogoutView,
)


urlpatterns = [
    path("auth/token/", TokenObtainPairView.as_view()),
    path("auth/token/refresh/", TokenRefreshView.as_view()),
    path("auth/sign-up/", RegistrationView.as_view()),
    path("auth/logout/", LogoutView.as_view()),
    path("profile/", UserProfileView.as_view()),
    path("profile/update/", UpdateUserView.as_view()),
    path("profile/delete/", DeleteUserView.as_view()),
]
