from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
        ('O', 'Other'),
    )
    customer_id = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=20, choices=GENDER)
    age = models.IntegerField()


class Account(models.Model):
    TYPES = (
        ('current', 'Current'),
        ('savings', 'Savings'),
    )

    STATUS = (
        ('active', 'Active'),
        ('frozen', 'Frozen'),
        ('disabled', 'Disabled'),
    )
    number = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=50, choices=TYPES)
    status = models.CharField(max_length=50, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)