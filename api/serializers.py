from rest_framework import serializers
from .models import User, Account, Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': { 'write_only': True },
        }
      
    def create(self, valiated_data):
        user = User(**valiated_data)
        user.set_password(valiated_data['password'])
        user.save()
        return user


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'