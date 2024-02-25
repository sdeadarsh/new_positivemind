from django.db import models


# Create your models here.

class Admin(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    address_id = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_id = models.PositiveIntegerField(null=True, blank=True)
    updated_by_id = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=1)
    user_type = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        db_table = "admin"


class UserType(models.Model):
    user_type = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "user_type"
