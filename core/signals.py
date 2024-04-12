import string
import random

from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Account


@receiver(pre_save, sender=Account)
def generate_account_number(sender, instance, **kwargs):
    """Generates account number"""
    if not instance.number:
        number = ''.join(random.choices(string.digits + string.ascii_letters, k=12))
        instance.number = number
        return number
