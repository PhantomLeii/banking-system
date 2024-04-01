from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, HyperlinkedIdentityField
from .models import User, Account, Transaction


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'date_joined',  'last_login', 'is_staff',
            'is_active', 'is_superuser', 'groups',
            'user_permissions',
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

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        exclude = ('owner',)

    def update(self, instance, validated_data):
        instance.number = validated_data.get('number', instance.number)
        if not instance.name:
            instance.name = instance.number
        
        instance.account_type = validated_data.get('account_type', instance.account_type)
        instance.status = validated_data.get('status', instance.status)
        instance.balance = validated_data.get('balance', instance.balance)
        return instance


class TransactionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'