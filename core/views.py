from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views.generic import TemplateView
from .forms import LoginForm
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