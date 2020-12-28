from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.timezone import now
from comment.models import Comment


class Post(models.Model):
    body = models.TextField(null=True)
    user_id = models.IntegerField(null=True)
    group_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=now)
    status = models.IntegerField(default=1)
    comments = GenericRelation(Comment)


class Photo(models.Model):
    post_id = models.IntegerField(null=True)
    user_id = models.IntegerField(null=True)
    photo = models.FileField(null=True, blank=True, upload_to='photos/')


class SavePost(models.Model):
    post_id = models.IntegerField(null=True)
    user_id = models.IntegerField(null=True)


class Video(models.Model):
    post_id = models.IntegerField(null=True)
    user_id = models.IntegerField(null=True)
    video = models.FileField(null=True, blank=True, upload_to='videos/')


class Following(models.Model):
    user_id = models.IntegerField(null=True)
    following_id = models.IntegerField(null=True)
    status = models.IntegerField(null=True, blank=True, default=1)


class Reaction(models.Model):
    user_id = models.IntegerField(null=True)
    post_id = models.IntegerField(null=True)
    think = models.IntegerField(null=True, blank=True)
    Lovely = models.IntegerField(null=True, blank=True)
    haha = models.IntegerField(null=True, blank=True)
    happy = models.IntegerField(null=True, blank=True)
    sad = models.IntegerField(null=True, blank=True)
    love = models.IntegerField(null=True, blank=True)
    like = models.IntegerField(null=True, blank=True)


class PostComment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='user')
    content = models.TextField(null=True, blank=True)
    publish = models.DateTimeField(default=now)
    status = models.BooleanField(default=True)

