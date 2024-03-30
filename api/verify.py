import jwt
from config import settings

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.middleware.csrf import CsrfViewMiddleware
from django.contrib.auth import get_user_model


class CSRFCheck(CsrfViewMiddleware):
    def _reject(self, request, reason):
        return reason
    

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        User = get_user_model()
        authorization_header = request.headers.get('Authorization')

        if not authorization_header:
            return None
        try:
            access_token = authorization_header.split(' ')[1]
            payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(
                'access token expired'
            )
        except IndexError:
            raise exceptions.AuthenticationFailed(
                'Token prefix missing'
            )
        
        try:
            user = User.objects.get(customerID=payload['customerID'])
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed(
                'User not found'
            )
        
        self.enforce_csrf(request)
        return (user, None)
    
    def enforce_csrf(self, request):
        check = CSRFCheck(get_response=None)
        check.process_request(request)
        reason = check.process_view(request, None, (), {})
        print(reason)

        if reason:
            raise exceptions.PermissionDenied('CSRF failed: %s' % reason)