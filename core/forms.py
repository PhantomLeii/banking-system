from typing import Any, Mapping
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
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
    def __init__(self, user, *args, **kwargs):
        super(WithdrawForm, self).__init__(*args, **kwargs)
        self.fields['account'].choices = self.get_account_choices(user)
    
    def get_account_choices(self, user):
        all_accounts = Account.objects.filter(user=user)
        choices = [(account.id, account.name.upper()) for account in all_accounts]
        return choices
    
    account = forms.ChoiceField(choices=(), widget=forms.Select(attrs={'class': 'form-control'}))
    amount = forms.DecimalField(max_digits=10, decimal_places=2)