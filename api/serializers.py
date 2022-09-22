from rest_framework.serializers import ModelSerializer, ValidationError
from django.contrib.auth.models import User
from django.core import exceptions
import django.contrib.auth.password_validation as validators


class UserSerializer(ModelSerializer):

    def validate_password(self, value):
        try:
            validators.validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return value

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
        return user

    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 
            'is_active', 'last_login', 'is_superuser', 'password'
        ]
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'is_superuser': {'read_only': True},
            'last_login': {'read_only': True}
        }