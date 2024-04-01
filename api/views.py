from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework import exceptions

from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import get_user_model
from .models import Account, Transaction
from .serializers import UserSerializer, AccountSerializer, TransactionSerializer
from .auth import generate_refresh_token, generate_access_token


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login_view(request):
    """Authenticate user & generate access & refresh tokens"""
    user = get_user_model()
    email = request.data.get('email')
    password = request.data.get('password')
    response = Response()

    if (email is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'email & password required'
        )
    
    try:
        user = user.objects.get(email=email)
    except user.DoesNotExist:
        raise exceptions.AuthenticationFailed(
            'User not found'
        )
    
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed(
            'Invalid password'
        )
    
    serializer = UserSerializer(user).data

    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)

    response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    response.data = {
        'accesToken': access_token,
        'user': serializer,
    }
    return response

@api_view(['POST'])
@permission_classes([AllowAny])
def logout_view(request):
    """Logout user"""
    response = Response()
    response.delete_cookie(key='refreshtoken')
    return Response({
        'detail': 'Success'
    }, status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def signup_view(request):
    """Register new user"""
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'detail': 'Success',
                'user': serializer.data
            }, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UserAPIView(APIView):
    def get(self, request):
        """List all user data"""
        user = request.user
        serialized_user = UserSerializer(user).data
        return Response({
            'user': serialized_user,
        }, status.HTTP_200_OK)
    
    def patch(self, request):
        """Partially update user data"""
        User = request.user
        serializer = UserSerializer(User, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'detail': 'success',
                'user': serializer.data
            }, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        """Delete existing user"""
        User = request.user
        User.delete()
        return Response({
            'detail': 'Success',
        }, status.HTTP_204_NO_CONTENT)