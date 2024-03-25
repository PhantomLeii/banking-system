from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User, Account, Transaction


class UserAPView(APIView):
    def get_user(self, request) -> User:
        '''
        Read user credentials from request
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