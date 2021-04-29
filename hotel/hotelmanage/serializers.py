from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import EmployeeApi
from logging import getLogger

logger = getLogger(__name__)


class EmployeeSerializers(serializers.ModelSerializer):
    username = serializers.CharField(required=False, max_length=225)
    email = serializers.EmailField(required=False, max_length=225, allow_null=False)
    password = serializers.CharField(required=False, max_length=225, allow_null=False)


    class Meta:
        model = EmployeeApi
        fields = ('username', 'email', 'password')

    def validate(self, attrs):
        username = attrs.get('username', None)
        password = attrs.get('password', None)

        if username is not None and not username.isalpha():
            logger.error(f'Name should be accept only Alphabets')
            raise serializers.ValidationError(f'Name should be accept only Alphabets')
        if password is None:
            logger.error(f'mobile number should be ENTER')
            raise serializers.ValidationError(f'Name should be EMPTY')
        return attrs