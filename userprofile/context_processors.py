from django.contrib.auth.models import User
from django_private_chat.models import Dialog, Message

from .models import ProfileImage
from django.contrib.auth.decorators import login_required

from web.models import WebsiteLogo, WebsiteFavIcon

from post.models import Following


def access_banner_image(request):
    logos = WebsiteLogo.objects.filter()
    icons = WebsiteFavIcon.objects.filter()

    logo = None
    for val in logos:
        logo = val.logo

    icon = None
    for val in icons:
        icon = val.icon

    context = {
        'logo': logo,
        'icon': icon
    }

    return context


def all_friend_re(request):
    friend_req = Following.objects.filter(following_id=request.user.id)
    context = {
        'friend_req': friend_req
    }
    # print(friend_req)
    return context


def all_friend(request):
    friend_req = Following.objects.filter(following_id=request.user.id, status=2)
    context = {
        'followers': friend_req
    }
    return context


def unread_message(request):
    msg = Dialog.objects.filter(opponent_id=request.user.id)

    message = []
    for value in msg:
        message = Message.objects.filter(dialog_id=value.id, read=0)

    dta = len(message)

    context = {
        'un_msg': dta,
        'message': message
    }
    return context