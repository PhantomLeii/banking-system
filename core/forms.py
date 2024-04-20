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


class UpdateUserForm(forms.Form):
    class Meta:
        model = User
        fields = "__all__"


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
    def __init__(self, user, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['recipient'].choices = self.get_recipient_choices(user)
        self.fields['sender'].choices = self.get_sender_choices(user)
    
    def get_recipient_choices(self, request_user):
        all_users = User.objects.all()
        choices = [(user.id, user.email) for user in all_users if user != request_user]
        return choices
    
    def get_sender_choices(self, user):
        sender_accounts = Account.objects.filter(user=user)
        choices = [(sender.id, sender.name) for sender in sender_accounts if sender.balance > 0]
        return choices
    
    sender = forms.ChoiceField(choices=(), widget=forms.Select(attrs={'class': 'form-control'}))
    recipient = forms.ChoiceField(choices=(), widget=forms.Select(attrs={'class': 'form-contron'}))
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    reference = forms.CharField(max_length=255)