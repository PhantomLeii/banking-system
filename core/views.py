from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Account, Transaction
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'routes/index.html'