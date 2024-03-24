from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet, basename='user')
router.register(r'accounts', views.AccountViewSet, basename='accounts')
router.register(r'transactions', views.TransactionViewSet, basename='transactions')

urlpatterns = [ path('', include(router.urls)) ]
