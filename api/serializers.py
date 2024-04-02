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

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        if not instance.name:
            instance.name = validated_data.get('number')
            instance.save()
            return instance
        instance.save()
        return instance

class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'