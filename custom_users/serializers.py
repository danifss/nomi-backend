from rest_framework import serializers
from custom_users.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('is_superuser', 'password', 'is_staff', 'groups', 'user_permissions')
