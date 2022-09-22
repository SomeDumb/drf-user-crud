from django.contrib.auth.models import User
from django.core import exceptions
import django.contrib.auth.password_validation as validators
from rest_framework.serializers import ModelSerializer, ValidationError


class UserSerializer(ModelSerializer):

    def validate(self, data):
        user = User(**data)
        password = data.get('password')
        errors = dict()

        try:
            validators.validate_password(password=password, user=user)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
        if errors:
            raise ValidationError(errors)
        return super(UserSerializer, self).validate(data)

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
