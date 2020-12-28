from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.http import HttpResponse
from post.models import Following


class AddFriendView(View):
    def get(self, request, to_username):
        Following.objects.create(following_id=to_username, user_id=request.user.id, status=1)
        return redirect('user:profile')


class UnfollowFriendView(View):
    def get(self, request, to_username):
        user_id = User.objects.get(pk=to_username)
        data = Following.objects.get(user_id=user_id.id, following_id=request.user.id)
        data.status = 2
        data.save()
        return redirect('user:profile')


class RemoveFriendView(View):
    def get(self, request, to_username):
        user_id = User.objects.get(pk=to_username)
        data = Following.objects.get(user_id=user_id.id, following_id=request.user.id)
        data.delete()
        return redirect('user:profile')


class FriendListView(View):
    def get(self, request):
        data = Following.objects.filter(following_id=request.user.id)
        context = {
            'friends': data
        }
        return render(request, 'profile/friend_list.html', context)

