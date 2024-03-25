from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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


class AccountAPIView(APIView):
    pass


class TransactionAPIView(APIView):
    pass