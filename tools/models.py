from django.contrib.auth.models import User
from django.db import models

# Create your models here.
GEEKS_CHOICES = (
    ("1", "Active"),
    ("2", "Deactivate"),
)


class AutoFriend(models.Model):
    user = models.TextField(null=True, blank=True, help_text="user name(s), sperated by a comma (,)")
    status = models.CharField(max_length=5, choices=GEEKS_CHOICES, default=1)


class AutoGroupJoin(models.Model):
    group = models.TextField(null=True, blank=True, help_text="group name(s), sperated by a comma (,)")
    status = models.CharField(max_length=5, choices=GEEKS_CHOICES, default=1)


class AutoPageLike(models.Model):
    page = models.TextField(null=True, blank=True, help_text="page name(s), sperated by a comma (,)")
    status = models.CharField(max_length=5, choices=GEEKS_CHOICES, default=1)
