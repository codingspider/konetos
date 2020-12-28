from django.db import models
from django.utils.timezone import now

GEEKS_CHOICES = (
    ("1", "Active"),
    ("2", "Deactivate"),
)


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=5, choices=GEEKS_CHOICES, default=1)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name


class Channel(models.Model):
    user_id = models.IntegerField(null=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    profile = models.ImageField(null=True, blank=True, upload_to='channel/profile/')
    cover = models.ImageField(null=True, blank=True, upload_to='channel/cover/')
    status = models.CharField(max_length=5, choices=GEEKS_CHOICES, default=1)
    created_at = models.DateTimeField(default=now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class ChannelThumbnail(models.Model):
    user_id = models.IntegerField(null=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='channel/thumbnail/')
    created_at = models.DateTimeField(default=now)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True, blank=True)


class ChannelCover(models.Model):
    user_id = models.IntegerField(null=True)
    cover = models.ImageField(null=True, blank=True, upload_to='channel/thumbnail/')
    created_at = models.DateTimeField(default=now)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True, blank=True)


