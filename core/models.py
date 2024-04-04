from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    ETHNICITY_CHOICES = (
        ('black', 'Black'),
        ('white', 'White'),
        ('other', 'Other'),
    )
    username = None
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    ethnicity = models.CharField(max_length=10, choices=ETHNICITY_CHOICES)
    street_number = models.IntegerField(blank=True, null=True)
    street_name = models.CharField(max_length=255, blank=True, null=True)
    suburb = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('name', 'surname', 'gender', 'city', 'phone_number')

    objects = UserManager()

    def __str__(self):
        return self.email


class Account(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('closed', 'Closed'),
        ('frozen', 'Frozen'),
    )

    TYPE_CHOICES = (
        ('current', 'Current'),
        ('savings', 'Savings'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=12, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f'{self.name} | {self.number}'


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction = models.ForeignKey('self', on_delete=models.CASCADE, related_name='related_transactions', null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'Transaction {self.timestamp}'
