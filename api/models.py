from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(
            self,
            email,
            firstName,
            lastName,
            phoneNumber,
            password,
            **other_fields
    ):
        if not email:
            raise ValueError('User must have an email')
    
        email = self.normalize_email(email)
        
        user = self.model(
            email=email,
            firstName=firstName,
            lastName=lastName,
            phoneNumber=phoneNumber,
            **other_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(
            self,
            email,
            firstName,
            lastName,
            phoneNumber,
            password,
            **other_fields
    ):
        if other_fields.get('is_staff') is not True:
            raise ValueError('Super user muct be staff')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Super user must be superuser')
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(
            email,
            firstName,
            lastName,
            phoneNumber,
            password,
            **other_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    username = None
    email = models.EmailField(max_length=255, unique=True)
    customer_id = models.CharField(max_length=50, unique=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER)
    age = models.IntegerField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'first_name',
        'last_name',
    )

    def __str__(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'


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

    def __str__(self):
        user_name = self.owner.__str__()
        return f'{user_name}: {self.number}'


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=50, unique=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        account = self.account.number
        return f'[{self.transaction_id}]: {self.account.number} => R {self.amount}'