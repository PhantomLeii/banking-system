from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer, ProfileSerializer

User = get_user_model()


class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny,)


class UserProfileView(RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user
