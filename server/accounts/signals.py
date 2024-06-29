from django.db.models.signals import pre_save
from django.dispatch import receiver
from random import randint

from .models import Account


@receiver(pre_save, sender=Account)
def generate_account_number(sender, instance, **kwargs):
    if not instance.account_number:
        starting_number = randint(31, 55)
        remaining_numbers = "".join(str(randint(0, 9)) for _ in range(13))
        instance.account_number = f"{starting_number}{remaining_numbers}"
