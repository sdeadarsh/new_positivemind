from django.db import models
import config


# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    address_id = models.PositiveIntegerField(null=True, blank=True)
    document_id = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_id = models.PositiveIntegerField(null=True, blank=True)
    updated_by_id = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=1)
    allergies = models.CharField(max_length=200, null=True, blank=True)
    disabilities = models.CharField(max_length=200, null=True, blank=True)
    device_implants = models.BooleanField(default=1)
    marital_status = models.PositiveIntegerField(choices=config.MARITAL_CHOICES, default=0)
    occupation = models.CharField(max_length=200, null=True, blank=True)
    nationality = models.CharField(max_length=200, null=True, blank=True)
    payer = models.CharField(max_length=200, null=True, blank=True)
    user_type = models.PositiveIntegerField(null=True, blank=True)
    about = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = "patient"


class Document(models.Model):
    document_url = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_id = models.PositiveIntegerField(null=True, blank=True)
    updated_by_id = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "document"
