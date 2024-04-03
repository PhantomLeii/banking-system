from django.contrib.auth import get_user_model
from .models import Account
from rest_framework import status
from typing import Any

def is_owner(request: Any, account: Account) -> bool:
    """
    Allow data transfer only if user endpoint user is
    rightful owner of account/accounts
    """
    try:
        user = get_user_model().objects.get(email=request.user)
    except:
        return False
    
    if account not in Account.objects.filter(owner=user):
        return False
    
    return True