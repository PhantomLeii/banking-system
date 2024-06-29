from rest_framework import serializers
from .models import Account


class CreatAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
        read_only_fields = (
            "account_number",
            "balance",
            "created_at",
            "is_active",
            "user",
        )

    def create(self, validated_data):
        account = Account.objects.create(**validated_data)
        return account


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
