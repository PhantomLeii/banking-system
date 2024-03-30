import jwt
from config import settings

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.utils.deprecation import MiddlewareMixin
from django.middleware.csrf import CsrfViewMiddleware
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model


class CSRFCheck(MiddlewareMixin):
    def __init__(self, get_response=None):
        super().__init__(get_response)
    
    def process_view(
            self,
            request,
            callback,
            callback_args,
            callback_kwargs
    ):
        if getattr(callback, 'csrf_exempt', False):
            return None
        
        if request.method not in ('GET', 'HEAD', 'OPTIONS', 'TRACE'):
            csrf_middleware = CsrfViewMiddleware()
            if not csrf_middleware.process_view(
                    request,
                    callback,
                    callback_args,
                    callback_kwargs
            ):
                return self._reject(request)
        return None
    
    def _reject(self, request):
        return HttpResponseForbidden('CSRF verification failed')
    

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
        
        return (user, None)
    
    def enforce_csrf(self, request):
        check = CSRFCheck()
        check.process_request(request)
        reason = check.process_view(request, None, (), {})
        print(reason)

        if reason:
            raise exceptions.PermissionDenied('CSRF failed: %s' % reason)