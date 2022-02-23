from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    lastUpdated = models.DateField(default=timezone.now)
    language = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    description = models.CharField(max_length=120)
    previewImage  = models.ImageField(null=True, blank=True)