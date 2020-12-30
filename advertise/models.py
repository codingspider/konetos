from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from chanel.models import Channel

GEEKS_CHOICES = (
    ("1", "Active"),
    ("2", "Deactivate"),
)

GENDER_CHOICES = (
    ("1", "Male"),
    ("2", "Female"),
)


class Country(models.Model):
    name = models.CharField(max_length=50, null=True)
    code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    header = models.TextField(null=True, blank=True, help_text="Appears on all pages right under the nav bar")
    sidebar = models.TextField(null=True, blank=True, help_text="Appears on the bottom of home sidebar")
    footer = models.TextField(null=True, blank=True, help_text="Appears on the bottom of home footer")
    post = models.TextField(null=True, blank=True, help_text="Appears in posts are loaded")
    status = models.CharField(max_length=5, choices=GEEKS_CHOICES, default=1)


class Campaign(models.Model):
    status = models.CharField(max_length=5, choices=GEEKS_CHOICES, default=1)
    created_at = models.DateTimeField(null=True, blank=True, default=now)
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES, default=0)
    placement = models.TextField(max_length=255, null=True, blank=True)
    bidding = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    page = models.ForeignKey(Channel, on_delete=models.CASCADE,null=True, blank=True )
    audience = models.ForeignKey(Country, on_delete=models.CASCADE,null=True, blank=True )
    start = models.CharField(max_length=255, null=True, blank=True)
    end = models.CharField(max_length=255, null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to='campaign/')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True )

    def __str__(self):
        return self.title




