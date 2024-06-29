from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Account(models.Model):
    ACCOUNT_TYPE = (
        ("Savings", "Savings"),
        ("Current", "Current"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPE)
    account_number = models.CharField(max_length=50, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.account_number
