from datetime import datetime, timedelta, UTC
from config import settings
import jwt

def generate_access_token(user):
    """Generate JWT access token for user"""
    payload = {
        'customerID': user.customerID,
        'exp': datetime.now(UTC) + timedelta(minutes=30),
        'iat': datetime.now(UTC),
    }

    access_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return access_token


def generate_refresh_token(user):
    payload = {
        'customerID': user.customerID,
        'exp': datetime.now(UTC) + timedelta(days=1),
        'iat': datetime.now(UTC),
    }

    refresh_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return refresh_token