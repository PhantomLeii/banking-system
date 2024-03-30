from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework import exceptions

from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import get_user_model

from .models import User, Account, Transaction
from .serializers import UserSerializer, AccountSerializer, TransactionSerializer
from .auth import generate_refresh_token, generate_access_token
from .utils import get_user_object


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
    except User.DoesNotExist:
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


class UserAPIView(APIView):
    def get(self, request):
        """Collect user data"""
        user = request.user
        serializer = UserSerializer(user).data
        return Response({
            'user': serializer,
        }, status.HTTP_200_OK)