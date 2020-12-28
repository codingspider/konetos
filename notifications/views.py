from django.contrib.auth.models import User
from django.shortcuts import render
from notify.signals import notify
from django.http import HttpResponse


def follow_user(request):
    user = 2
    user = User.objects.get(pk=user)
    notify.send(request.user, recipient=user, actor=request.user, verb='followed you.', nf_type='followed_by_one_user')

    return HttpResponse('ok')


def upload_video(request):
    video = ''
    followers = list(request.user.followers())

    notify.send(request.user, recipient_list=followers, actor=request.user, verb='uploaded.', target=video, nf_type='video_upload_from_following')

    return HttpResponse('ok')