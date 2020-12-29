from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from groups_manager.models import Group, Member, GroupMember
from .models import GroupOwner, GroupProfileImage, GroupCoverImage
from post.models import Post


class GroupListView(View):

    def get(self, request):
        data = GroupOwner.objects.filter(user_id=request.user.id)
        if data:
            for val in data:
                id = val.group_id

            groups = Group.objects.filter(id=id)
            member = GroupMember.objects.filter(group_id=id).count()

            try:
                photo = GroupProfileImage.objects.get(group_id=id)
            except GroupProfileImage.DoesNotExist:

                photo = None

            try:
                cover = GroupCoverImage.objects.get(group_id=id)
            except GroupCoverImage.DoesNotExist:
                cover = None

            context = {
                'groups': groups,
                'member': member,
                'profile': photo,
                'cover': cover

            }
        else:
            groups = []
            member = []
            photo = ''
            cover = ''
            context = {
                'groups': groups,
                'member': member,
                'owner': data,
                'photo': photo,
                'cover': cover
            }
        return render(request, 'group/list.html', context)


class GroupMemberCreateView(View):
    def post(self, request):
        id = request.POST.get('group_id')
        project_main = Group.objects.get(pk=id)
        staff = Group.objects.create(name='Staff', parent=project_main)
        user = User.objects.get(pk=request.user.id)
        john = Member.objects.create(first_name=user.username, last_name=user.username)
        staff.add_member(john)
        return redirect('user:profile')


class CreateGroupView(View):
    def get(self, request):
        return render(request, 'group/create_group.html')

    def post(self, request):
        name = request.POST.get('name')
        instance = Group.objects.create(name=name)
        id = instance.pk
        data = GroupOwner.objects.create(user_id=request.user.id, group_id=id)
        return render(request, 'group/create_group.html')


class ManageGroupView(View):
    def get(self, request, pk):
        posts = Post.objects.filter(user_id=request.user.id, status=1, group_id=pk).order_by('-id')

        profiles = GroupProfileImage.objects.filter(user_id=request.user.id, group_id=pk)
        covers = GroupCoverImage.objects.filter(user_id=request.user.id, group_id=pk)
        datalen = len(profiles)
        data2len = len(covers)
        if datalen > 0:
            for val in profiles:
                profile = val.profile
        else:
            profile = ''

        if data2len > 0:
            for x in covers:
                cover = x.cover
        else:
            cover = ''

        context = {
            'pk': pk,
            'posts': posts,
            'cover': cover,
            'profile': profile
        }

        return render(request, 'group/manage_group.html', context)


class SettingGroupView(View):
    def get(self, request, pk):
        try:
            profiles = GroupProfileImage.objects.filter(user_id=request.user.id, group_id=pk)
            covers = GroupCoverImage.objects.filter(user_id=request.user.id, group_id=pk)
            datalen = len(profiles)
            data2len = len(covers)
            if datalen > 0:
                for val in profiles:
                    profile = val.profile

            else:
                profile = ''

            if data2len > 0:
                for x in covers:
                    cover = x.cover
            else:
                cover = ''

            context = {
                'pk': pk,
                'profile': profile,
                'cover': cover
            }
        except GroupProfileImage.DoesNotExist:
            context = {'pk': pk}
            return context

        return render(request, 'group/group_setting.html', context)


class GroupProfileImageView(View):
    @method_decorator(login_required)
    def post(self, request):
        if self.request.FILES:
            profile = request.FILES['profile']
            id = request.POST.get('group_id')

            data = GroupProfileImage.objects.filter(user_id=request.user.id, group_id=id)

            datalen = len(data)

            if datalen > 0:
                upd = GroupProfileImage.objects.get(user_id=request.user.id, group_id=id)
                upd.profile = profile
                upd.user_id = request.user.id
                upd.save()

            else:
                GroupProfileImage.objects.create(profile=profile, user_id=request.user.id, group_id=id)
            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:
            return JsonResponse({"error": 500}, json_dumps_params={'indent': 2})


class GroupCoverImageCreate(View):
    @method_decorator(login_required)
    def post(self, request):
        if self.request.FILES:
            cover = request.FILES['cover']
            id = request.POST.get('group_id')

            data = GroupCoverImage.objects.filter(user_id=request.user.id, group_id=id)

            datalen = len(data)

            if datalen > 0:
                upd = GroupCoverImage.objects.get(user_id=request.user.id, group_id=id)
                upd.cover = cover
                upd.user_id = request.user.id
                upd.group_id = id
                upd.save()

            else:
                GroupCoverImage.objects.create(cover=cover, user_id=request.user.id, group_id=id)
            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:
            return JsonResponse({"error": 500}, json_dumps_params={'indent': 2})


class GroupMemberView(View):
    def get(self, request, pk):
        members = GroupMember.objects.filter(group_id=pk)
        context ={
            'members': members
        }
        return render(request, 'group/members.html', context)