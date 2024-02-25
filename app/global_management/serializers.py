from rest_framework import serializers
from .models import Thinking, ThinkingMaster, QuestionerMaster, Questioner, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class QuestionerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questioner
        fields = "__all__"


class QuestionerMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionerMaster
        fields = "__all__"


class ThinkingMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThinkingMaster
        fields = "__all__"


class ThinkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thinking
        fields = "__all__"
