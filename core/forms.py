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


class AccountForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields['account'].choices = self.get_account_choices(user)
    
    def get_account_choices(self, user):
        all_accounts = Account.objects.filter(user=user)
        choices = [(account.id, account.name) for account in all_accounts]
        return choices
    
    account = forms.ChoiceField(choices=(), widget=forms.Select(attrs={'class': 'form-control'}))
    amount = forms.DecimalField(max_digits=10, decimal_places=2)


class WithdrawForm(AccountForm):
    def get_account_choices(self, user):
        all_accounts = Account.objects.filter(user=user)
        choices = [(account.id, account.name.upper()) for account in all_accounts if account.balance > 0]
        return choices


class DepositForm(AccountForm):
    pass


class PaymentForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['recipient'].choices = self.get_recipient_choices()
    
    def get_recipient_choices(self):
        all_users = User.objects.all()
        choices = [(user.id, user.email) for user in all_users]
        return choices
    
    def clean(self):
        cleaned_data = super().clean()
        recipeient_id = cleaned_data.get('recipient')
        recipeient_user = User.objects.get(id=recipeient_id)

        recipient_account = Account.objects.filter(user=recipeient_user).first()
        if not recipient_account:
            raise forms.ValidationError('Recipient has no active accounts')
        cleaned_data['recipient_account'] = recipient_account
        return cleaned_data
    
    recipient = forms.ChoiceField(choices=(), widget=forms.Select(attrs={'class': 'form-contron'}))
    amount = forms.DecimalField(max_digits=10, decimal_places=2)    