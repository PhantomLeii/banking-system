import string
import random

from django.db.models.signals import post_init
from django.dispatch import receiver
from .models import Account


@receiver(post_init, sender=Account)
def generate_account_number(sender, instance, **kwargs):
    """Generates account number"""
    if not instance.number:
        number = ''.join(random.choices(string.digits + string.ascii_letters, k=12))
        instance.number = number
        instance.save()
        return number
