from .models import User
from rest_framework import status
from typing import Any

user_email = 'phoshokolebogang@outlook.com'

def get_user_object(request: Any) -> User:
  """Pull user object from authorization payload"""
  try:
      user = User.objects.get(email=user_email)
  except User.DoesNotExist:
      return None