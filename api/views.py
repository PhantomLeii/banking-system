from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import User, Account, Transaction
from .serializers import UserSerializer


class UserAPIView(APIView):
    def post(self, request):
        '''
        Register new user
        '''
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request):
        '''
        View all user profile data
        '''
        users = User.objects.get(id=1)
        serializer = UserSerializer(users)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def patch(self, request):
        '''
        Partialy update user profile data
        '''
        pass

    def delete(self, delete):
        '''
        Delete current user profile
        '''
        pass


class AccountAPIView(APIView):
    pass


class TransactionAPIView(APIView):
    pass