from django.db import models
import config


# Create your models here.
class ThinkingMaster(models.Model):
    question = models.CharField(max_length=200, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_id = models.PositiveIntegerField(null=True, blank=True)
    updated_by_id = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "thinking_master"


class Thinking(models.Model):
    question_id = models.PositiveIntegerField(null=True, blank=True)
    rating = models.PositiveIntegerField(choices=config.RATING_CHOICES, default=0)
    rated_by_id = models.PositiveIntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    created_by_id = models.PositiveIntegerField(null=True, blank=True)
    updated_by_id = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "thinking"


class Address(models.Model):
    city = models.CharField(max_length=200, null=True, blank=True)
    sub_district = models.CharField(max_length=200, null=True, blank=True)
    district = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = "address"


class QuestionerMaster(models.Model):
    question = models.CharField(max_length=200, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    created_by_id = models.PositiveIntegerField(null=True, blank=True)
    updated_by_id = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "questioner_master"


class Questioner(models.Model):
    question_id = models.PositiveIntegerField(null=True, blank=True)
    patient_id = models.PositiveIntegerField(null=True, blank=True)
    response = models.PositiveIntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    created_by_id = models.PositiveIntegerField(null=True, blank=True)
    updated_by_id = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "questioner"

