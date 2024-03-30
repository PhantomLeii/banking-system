from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import User, Account, Transaction
from .serializers import UserSerializer, AccountSerializer, TransactionSerializer
from utils import get_user_object


class CreateUserView(CreateAPIView):
    """Create user with no required permissions"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAPIView(APIView):
    authentication_classes = []
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """View all user profile data"""
        instance = get_user_object(request)
        if instance is None:
            return Response({
                'detail': 'User not found',
            }, status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(instance)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request):
        """Partially update user profile data"""
        instance = get_user_object(request)
        serializer = UserSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request):
        """Delete current user profile"""
        instance = get_user_object(request)
        instance.delete()
        return Response({
            'detail': 'Deleted successfully'
        }, status.HTTP_204_NO_CONTENT)


def get_user_accounts(request):
    """Isolate accounts owned by current user"""
    user = get_user_object(request)
    accounts = Account.objects.filter(user_id=user)
    if accounts:
        return accounts
    return Response({
        'detail': 'No accounts'
    }, status.HTTP_204_NO_CONTENT)


class AccountAPIView(APIView):
    pass


class TransactionAPIView(APIView):
    pass
