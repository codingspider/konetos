from django.db import models


class GroupOwner(models.Model):
    user_id = models.IntegerField(null=True)
    group_id = models.IntegerField(null=True)


class GroupProfileImage(models.Model):
    profile = models.ImageField(null=True, upload_to='group/profile/')
    user_id = models.IntegerField(null=True)
    group_id = models.IntegerField(null=True)


class GroupCoverImage(models.Model):
    cover = models.ImageField(null=True, upload_to='group/cover/')
    user_id = models.IntegerField(null=True)
    group_id = models.IntegerField(null=True)