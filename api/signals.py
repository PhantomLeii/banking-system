from .models import User, Account, Transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid, string, random


@receiver(pre_save, sender=User)
def generate_customer_id(sender, instance, **kwargs):
  '''
  Generate UUID code
  '''
  if not instance.customerID:
      instance.customerID = str(uuid.uuid4())[:12].replace('-', '')


@receiver(pre_save, sender=Account)
def generate_account_number(sender, instance, **kwargs):
    '''
    Generate alphanumeric code
    '''
    if not instance.number:
       letters = ''.join(random.choices(string.ascii_letters, k=4)).upper()
       digits = ''.join(random.choices(string.digits, k=10))
       instance.number = f'{ letters }_{ digits }'


@receiver(pre_save, sender=Transaction)
def generate_transaction_id(sender, instance, **kwargs):
    '''
    Generate UUID code
    '''
    if not instance.transaction_id:
       instance.transaction_id = str(uuid.uuid4())[:10]