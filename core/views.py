from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .forms import LoginForm, RegisterForm, CreateAccountForm
from .models import User, Account, Transaction


class HomePageView(TemplateView):
    template_name = 'routes/index.html'

    def get(self, request):
       return render(request, self.template_name, {})


class LoginView(TemplateView):
    template_name = 'routes/login_form.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                error_message = None
                login(request, user)
                return redirect('home')
            else:
                error_message = 'Invalid email or password'
        else:
            error_message = 'Invalid form data'
        
        context = {'form': form, 'error_message': error_message}
        return render(request, self.template_name, context)
    

class LogoutView(TemplateView):
    template_name = 'routes/logout_form.html'

    def get(self, request):
        return render(request, self.template_name, {})
    
    def post(self, request):
        logout(request)
        return redirect('home')


class RegisterView(TemplateView):
    template_name = 'routes/register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            error_message = None
            form.save()
            return redirect('login')
        else:
            error_message = 'Invalid form data'
        context = {'form': form, 'error_message': error_message}
        return render(request, self.template_name, context)


class AccountsView(LoginRequiredMixin, TemplateView):
    template_name = 'routes/accounts.html'

    def get(self, request):
        accounts = Account.objects.filter(user=request.user)
        return render(request, self.template_name, {'accounts': accounts})


class CreateAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'routes/create_account.html'
    
    def get(self, request):
        form = CreateAccountForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            account_type = form.cleaned_data['account_type']

            account = Account.objects.create(
                user=request.user,
                name=name,
                account_type=account_type
            )
            return redirect('accounts')
        else:
            pass
        return render(request, self.template_name, {'form': form})


class AccountDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'routes/account_detail.html'

    def get(self, request, pk):
        account = Account.objects.get(id=pk)
        if account:
            transactions = Transaction.objects.filter(account=account).order_by('-timestamp')[:50]
        else:
            return redirect('not_found.html')
        context = {'account': account, 'transactions': transactions}
        return render(request, self.template_name, context)


class DeleteAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'routes/delete_account_form.html'

    def get_user_accounts(self, user, pk):
        accounts = Account.objects.filter(user=user)
        return accounts

    def get(self, request, pk):
        accounts = self.get_user_accounts(request.user, pk)
        try:
            account = Account.objects.get(id=pk)
            if account not in accounts:
                raise Account.DoesNotExist
        except Account.DoesNotExist:
            # return redirect('Account not found')
            pass
        return render(request, self.template_name, {'account': account})
    
    def post(self, request, pk):
        accounts = self.get_user_accounts(request.user, pk)
        try:
            account = Account.objects.get(id=pk)
            if account not in accounts:
                raise Account.DoesNotExist
            account.delete()
            return redirect('accounts')
        except Account.DoesNotExist:
            # return redirect('Account not found')
            pass
        return render(request, self.template_name, {'account': account})