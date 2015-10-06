from rest_framework import serializers
from core.models import Attribute, Profile
from custom_users.serializers import CustomUserSerializer

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute

class ProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    attributes = AttributeSerializer(many=True)

    class Meta:
        model = Profile

class RelationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    attributes = AttributeSerializer(many=True)

    class Meta:
        model = Profile
        exclude = ("connections",)
