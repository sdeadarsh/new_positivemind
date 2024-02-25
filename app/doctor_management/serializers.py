from rest_framework import serializers
from .models import Doctor, Precipitation, Appointment, AppointmentMaster, Feedback


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class PrecipitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precipitation
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"


class AppointmentMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentMaster
        fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"

