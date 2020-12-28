from django.db import models

# Create your models here.
from django.utils.timezone import now


class WebsiteLogo(models.Model):
    logo = models.ImageField(null=True, blank=True, upload_to='logo/')
    created_at = models.DateTimeField(default=now)


class WebsiteFavIcon(models.Model):
    icon = models.ImageField(null=True, blank=True, upload_to='icon/')
    created_at = models.DateTimeField(default=now)


class Privacy(models.Model):
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=now)


class Terms(models.Model):
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=now)