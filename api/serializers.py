from rest_framework import serializers
from .models import User, Account, Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': { 'write_only': True },
        }
      
    def create(self, valiated_data) -> User:
        password = valiated_data.pop('password', None)
        instance = self.Meta.model(**valiated_data)
        
        if password is not None:
            instance.set_password(password)
        
        instance.save()
        return instance

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'