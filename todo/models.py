from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=now)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, editable=False,null=True,blank=True)

    def __str__(self):
        return self.title