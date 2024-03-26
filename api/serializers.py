from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import User, Account, Transaction


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'date_joined',  'last_login', 'is_staff',
            'is_active', 'is_superuser',
        )
        extra_kwargs = {
            'password': { 'write_only': True },
        }
      
    def create(self, valiated_data):
        password = valiated_data.pop('password', None)
        instance = self.Meta.model(**valiated_data)
        
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class AccountSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class TransactionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'