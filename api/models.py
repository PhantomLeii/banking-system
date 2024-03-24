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
    pass