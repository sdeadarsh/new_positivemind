from rest_framework import serializers
from .models import Admin, UserType


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = "__all__"
