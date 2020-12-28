from django.contrib.auth.models import User
from django.shortcuts import render
from django.conf.urls import url
from django.http import HttpResponse

from tools.models import AutoFriend

from post.models import Following


def check(request):
    data = AutoFriend.objects.all()
    for val in data:
        value = str(val.user).split(",")

    for rok in value:
        auto_user = User.objects.filter(username=rok)
        for jui in auto_user:
            Following.objects.create(user_id=jui.id, following_id=1, status=1)
    return HttpResponse("ok")