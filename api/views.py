from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Account, Transaction
from .serializers import UserSerializer


class UserAPView(APIView):
    def post(self, request):
        '''
        Register new user
        '''
        serializer = UserSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.data, status.HTTP_201_CREATED)


class AccountAPIView(APIView):
    pass


class TransactionAPIView(APIView):
    pass