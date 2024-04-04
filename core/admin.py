from django.contrib import admin
from django.contrib.auth import get_user_model
from core.models import Account, Transaction

User = get_user_model()

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Transaction)
