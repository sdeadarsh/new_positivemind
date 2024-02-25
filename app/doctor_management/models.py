from django.db import models


# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    role = models.CharField(max_length=200, null=True, blank=True)
    experiences = models.CharField(max_length=200, null=True, blank=True)
    img = models.URLField(max_length=300)
    qualification = models.CharField(max_length=200, null=True, blank=True)
    address_id = models.PositiveIntegerField(null=True, blank=True)
    physical_treatment = models.CharField(max_length=200, null=True, blank=True)
    therapies = models.CharField(max_length=200, null=True, blank=True)
    medico_legal_report = models.CharField(max_length=200, null=True, blank=True)
    occupational_health_work = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_id = models.PositiveIntegerField(null=True, blank=True)
    updated_by_id = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=1)
    user_type = models.PositiveIntegerField(null=True, blank=True)
    specialties = models.PositiveIntegerField(null=True, blank=True)
    disorder = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        db_table = "doctor"


class Precipitation(models.Model):
    drug_form = models.PositiveIntegerField(null=True, blank=True)
    drug_name = models.PositiveIntegerField(null=True, blank=True)
    dose = models.PositiveIntegerField(null=True, blank=True)
    frequency = models.PositiveIntegerField(null=True, blank=True)
    route = models.PositiveIntegerField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    changes = models.BooleanField(default=1)
    patient_id = models.PositiveIntegerField(null=True, blank=True)
    doctor_id = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_id = models.PositiveIntegerField(null=True, blank=True)
    updated_by_id = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "precipitation"


class Feedback(models.Model):
    rating = models.PositiveIntegerField(null=True, blank=True)
    comment = models.CharField(max_length=200, null=True, blank=True)
    doctor_id = models.PositiveIntegerField(null=True, blank=True)
    user_id = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_id = models.PositiveIntegerField(null=True, blank=True)
    updated_by_id = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "feedback"


class Appointment(models.Model):
    patient_id = models.PositiveIntegerField(null=True, blank=True)
    doctor_id = models.PositiveIntegerField(null=True, blank=True)
    appointment_date = models.DateTimeField(null=True, blank=True)
    appointment_type = models.PositiveIntegerField(null=True, blank=True)
    appointment_mode = models.PositiveIntegerField(null=True, blank=True)
    language = models.PositiveIntegerField(null=True, blank=True)
    notes = models.CharField(max_length=200, null=True, blank=True)
    payment_id = models.PositiveIntegerField(null=True, blank=True)
    payment_status = models.BooleanField(default=1)
    prescription = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_id = models.PositiveIntegerField(null=True, blank=True)
    updated_by_id = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "appointment"


class AppointmentMaster(models.Model):
    type = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "appointment_master"
