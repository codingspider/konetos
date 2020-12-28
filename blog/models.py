from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.timezone import now
from slugify import unique_slugify
from django.contrib.contenttypes.fields import GenericRelation


class Blog(models.Model):
    title = models.CharField(max_length=255, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    short_description = models.TextField(null=True)
    description = models.TextField(null=True)
    thumbnail = models.ImageField(null=True, upload_to='blog/')
    created_at = models.DateTimeField(default=now)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, editable=False,null=True,blank=True)
    likes = models.IntegerField(null=True, blank=True, default=0)
    visit = models.IntegerField(null=True, blank=True, default=0)

    def save(self,*args, **kwargs):
        slug_str = "%s" % (self.title,)
        unique_slugify(slug_str)
        super(Blog, self).save()


