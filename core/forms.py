from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Account


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email'] + list(model.REQUIRED_FIELDS) + ['password1', 'password2']


class CreateAccountForm(forms.Form):
    name = forms.CharField(max_length=255)
    account_type = forms.ChoiceField(choices=Account.TYPE_CHOICES)


class WithdrawForm(forms.Form):
    ACCOUNTS:list|tuple|None = None

    acccount = forms.ChoiceField(choices=ACCOUNTS)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)