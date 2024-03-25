from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.views import obtain_jwt_token
from .models import User, Account, Transaction

ObtainJWTToken = obtain_jwt_token


class UserAPView(APIView):
    def get_user(self, request) -> User:
        '''
        Read user credentials from request
        authorization header
        '''
        pass    
    
    def get(self, request):
        '''
        View all user profile data
        '''
        pass        


class AccountAPIView(APIView):
    pass


class TransactionAPIView(APIView):
    pass