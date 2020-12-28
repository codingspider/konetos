from django.core import validators
from django.db import models
from birthday.fields import BirthdayField
from birthday.managers import BirthdayManager


class Contact(models.Model):
    username = models.CharField(max_length=255,null=True, blank=True)
    email = models.CharField(max_length=255,null=True, blank=True)
    mobile = models.CharField(max_length=255,null=True, blank=True)
    address = models.CharField(max_length=255,null=True, blank=True)
    website = models.CharField(max_length=255,null=True, blank=True)
    social_link = models.CharField(max_length=255,null=True, blank=True)
    birthday = models.CharField(max_length=255,null=True, blank=True)
    gender = models.CharField(max_length=255,null=True, blank=True)
    language = models.CharField(max_length=255,null=True, blank=True)
    interest = models.CharField(max_length=255,null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    # birthday = BirthdayField(null=True)
    # objects = BirthdayManager()


class Relation(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    member_id = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=255,null=True, blank=True)
    relation = models.CharField(max_length=255, blank=True, null=True)


class Work(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)


class Education(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    college = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)


class Address(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    current_city = models.CharField(max_length=255, blank=True, null=True)
    lived = models.CharField(max_length=255, blank=True, null=True)


class Details(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    about = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    quote = models.TextField(max_length=255, blank=True, null=True)


class ProfileImage(models.Model):
    profile = models.ImageField( blank=True, null=True, upload_to='profile/')
    cover = models.ImageField(blank=True, null=True, upload_to='cover/')
    user_id = models.IntegerField(null=True, blank=True)


class Events(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    user_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name