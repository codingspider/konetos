from django.db import models

# Create your models here.
GEEKS_CHOICES = (
    ("1", "Active"),
    ("2", "Deactivate"),
)


class Advertisement(models.Model):
    header = models.TextField(null=True, blank=True, help_text="Appears on all pages right under the nav bar")
    sidebar = models.TextField(null=True, blank=True, help_text="Appears on the bottom of home sidebar")
    footer = models.TextField(null=True, blank=True, help_text="Appears on the bottom of home footer")
    post = models.TextField(null=True, blank=True, help_text="Appears in posts are loaded")
    status = models.CharField(max_length=5, choices=GEEKS_CHOICES, default=1)