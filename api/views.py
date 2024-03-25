from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Account, Transaction
from .serializers import UserSerializer, AccountSerializer


def get_user_object(request):
    """Isolate user object"""
    try:
        user = User.objects.get(id=2)
    except User.DoesNotExist:
        return Response({
            'detail': 'User not found'
        }, status.HTTP_404_NOT_FOUND)
    return user


class UserAPIView(APIView):
    def post(request):
        """Register new user"""
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request):
        """View all user profile data"""
        instance = get_user_object(request)
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
    def get(self, request):
        """View owned bank account data"""
        accounts = get_user_accounts(request)
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TransactionAPIView(APIView):
    pass
