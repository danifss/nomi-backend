from rest_framework import serializers
from core.models import Attribute, Profile

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile