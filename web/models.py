from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    customer_id = models.CharField(max_length=50, unique=True)


class Account(models.Model):
    TYPES = (
        ('current', 'Current'),
        ('savings', 'Saving'),
    )
    number = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_add_now=True)
    account_type = models.CharField(max_length=50, choices=TYPES)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=50, unique=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_add_now=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)