from django.urls import path
from .views import UserAPIView, AccountAPIView, CreateUserView


urlpatterns = [
    path('user/', UserAPIView.as_view(), name='user'),
    path('signup/', CreateUserView.as_view(), name='user-signup'),
    path('account/', AccountAPIView.as_view(), name='account'),
]