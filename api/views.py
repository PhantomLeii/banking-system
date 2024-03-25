from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Account, Transaction
from .serializers import UserSerializer


class UserAPIView(APIView):
    def get_user_object(self, request):
        try:
            user = User.objects.get(id=1)
        except User.DoesNotExist:
            return Response({
                'detail': 'User not found'
            }, status.HTTP_404_NOT_FOUND)

        return user

    def post(self, request):
        """Register new user"""
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request):
        """View all user profile data"""
        instance = self.get_user_object(request)
        serializer = UserSerializer(instance)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request):
        """Partially update user profile data"""
        instance = self.get_user_object(request)

        serializer = UserSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request):
        """Delete current user profile"""
        instance = self.get_user_object(request)
        instance.delete()
        return Response({
            'detail': 'Deleted successfully'
        }, status.HTTP_204_NO_CONTENT)


class AccountAPIView(APIView):
    pass


class TransactionAPIView(APIView):
    pass
