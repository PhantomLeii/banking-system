from .models import User, Account
from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid


@receiver(pre_save, sender=User)
def generate_customer_id(sender, instance, **kwargs):
  '''
  Generate random UUID code for user identification.
  '''
  if not instance.customer_id:
      instance.customer_id = str(uuid.uuid4())[:12].replace('-', '')