from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


# Create your models here.
class CameraModel(models.Model):
    # Analytics Categories Defined In System
    ANALYTICS_CHOICES = [('PEDESTRIAN', 'Pedestrian Analytics'), ('VEHICLE', 'Vehicle Classification'), ('ALL', 'All')]

    # Model Fields for Camera Registry
    description = models.CharField(max_length=570)
    preferred_analytics = models.CharField(max_length=100, choices=ANALYTICS_CHOICES)
    title = models.CharField(max_length=270)
    rtvsp_url = models.CharField(max_length=1024)
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registered_by_user')
    is_active = models.BooleanField(default=False)
    added_on = models.DateTimeField(default=datetime.now())
