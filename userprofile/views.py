from django.conf.global_settings import LOGIN_REDIRECT_URL
from django.contrib import messages, auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.core.serializers import json
from django.db.models import Count
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Details, Address, Relation, Work, Education, ProfileImage, Events
# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from post.models import Post, Photo, Following, Video, PostComment
from django.db.models import Q
# from groups_manager.models import Group, Member
from notify.signals import notify
from dateutil import parser


class ProfileView(View):
    @method_decorator(login_required)
    def get(self, request):
        post = Post.objects.filter(user_id=request.user.id)
        total_post = post.aggregate(total_count=Count('id'))

        try:
            profile = ProfileImage.objects.get(user_id=request.user.id)
        except ProfileImage.DoesNotExist:
            profile = ""

        posts = Post.objects.filter(user_id=request.user.id, status=1).order_by('-id')

        photo = Photo.objects.filter(user_id=request.user.id).order_by('-id')
        following = Following.objects.filter(user_id=request.user.id).aggregate(total_following=Count('id'))
        total_follower = Following.objects.filter(following_id=request.user.id, status=2).aggregate(total_follower=Count('id'))
        work = Work.objects.filter(user_id=request.user.id)
        education = Education.objects.filter(user_id=request.user.id)
        all_fol = Following.objects.filter(following_id=request.user.id)
        id = request.user.id
        all_followers = []
        for value in all_fol:
            all_followers += User.objects.filter(pk=value.user_id)
        print(all_followers)


        context = {
            'total_post': total_post,
            'profile': profile,
            'photos': photo,
            'following': following,
            'total_follower': total_follower,
            'all_followers': all_followers,
            'userid': id,
            'posts': posts,
            'works': work,
            'educations': education
        }
        return render(request, 'profile/profile.html', context)


class LogoutView(View):
    @method_decorator(login_required)
    def get(self,request):
        auth.logout(request)
        messages.info(request, "Logged out successfully!")
        return redirect("/")


class ContactInformationView(View):
    @method_decorator(login_required)
    def post(self, request):
        if self.request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            website = request.POST.get('website')
            social = request.POST.get('social')
            birthday = request.POST.get('dob')
            language = request.POST.get('language')
            interest = request.POST.get('interest')
            gender = request.POST.get('gender')
            user_id = request.POST.get('user_id')

            data = Contact.objects.filter(
                user_id=user_id
            )
            cdata = len(data)

            if(cdata > 0):
                upd = Contact.objects.get(user_id=user_id)
                upd.username = username
                upd.email = email
                upd.mobile = phone
                upd.address = address
                upd.website = website
                upd.social_link = social
                upd.birthday = birthday
                upd.language = language
                upd.interest = interest
                upd.gender = gender
                upd.user_id = user_id
                upd.save()
                response = {
                    'success': 'Success!'
                }
            else:
                Contact.objects.create(
                    username=username,
                    email=email,
                    mobile=phone,
                    address=address,
                    website=website,
                    social_link=social,
                    birthday=birthday,
                    gender=gender,
                    language=language,
                    interest=interest,
                    user_id=user_id
                                       )
                response = {
                    'success': 'Success!'
                }
        else:
            response = {
                'error': 'something went wrong!'
            }
        return JsonResponse(response)



class DetailInformationView(View):
    @method_decorator(login_required)
    def post(self, request):
        if self.request.POST:
            name = request.POST.get('nick_name')
            about = request.POST.get('about')
            quote = request.POST.get('quote')
            user_id = request.POST.get('user_id')

            data = Details.objects.filter(
                user_id=user_id
            )
            cdata = len(data)

            if(cdata > 0):
                upd = Details.objects.get(user_id=user_id)
                upd.name = name
                upd.about = about
                upd.quote = quote
                upd.user_id = user_id
                upd.save()
                response = {
                    'success': 'Success!'
                }
            else:
                Details.objects.create(
                    name=name,
                    about=about,
                    quote=quote,
                    user_id=user_id
                                       )
                response = {
                    'success': 'Success!'
                }
        else:
            response = {
                'error': 'something went wrong!'
            }
        return JsonResponse(response)



class PlaceCreteView(View):
    @method_decorator(login_required)
    def post(self, request):
        if self.request.POST:
            lived = request.POST.get('lived')
            current_city = request.POST.get('current_city')
            user_id = request.POST.get('user_id')

            data = Address.objects.filter(
                user_id=user_id
            )
            cdata = len(data)

            if(cdata > 0):
                upd = Address.objects.get(user_id=user_id)
                upd.lived = lived
                upd.current_city = current_city
                upd.user_id = user_id
                upd.save()
                response = {
                    'success': 'Success!'
                }
            else:
                Address.objects.create(
                    lived=lived,
                    current_city=current_city,
                    user_id=user_id
                                       )
                response = {
                    'success': 'Success!'
                }
        else:
            response = {
                'error': 'something went wrong!'
            }
        return JsonResponse(response)


class RelationCreateView(View):
    @method_decorator(login_required)
    def post(self, request):
        if self.request.POST:
            status = request.POST.get('status')
            relation = request.POST.get('relation')
            member = request.POST.get('member')
            user_id = request.POST.get('user_id')

            data = Relation.objects.filter(
                user_id=user_id
            )
            cdata = len(data)

            if(cdata > 0):
                upd = Relation.objects.get(user_id=user_id)
                upd.status = status
                upd.relation = relation
                upd.user_id = user_id
                upd.member_id = member
                upd.save()
                response = {
                    'success': 'Success!'
                }
            else:
                Relation.objects.create(
                    status=status,
                    relation=relation,
                    member_id=member,
                    user_id=user_id
                                       )
                response = {
                    'success': 'Success!'
                }
        else:
            response = {
                'error': 'something went wrong!'
            }
        return JsonResponse(response)


class WorkCreateView(View):
    @method_decorator(login_required)
    def post(self, request):
        if self.request.POST:
            company = request.POST.get('company')
            designation = request.POST.get('designation')
            user_id = request.POST.get('user_id')

            Work.objects.create(
                company=company,
                designation=designation,
                user_id=user_id
            )
            response = {
                'success': 200
            }
            return redirect('user:profile')

        else:
            response = {
                'error': 'something went wrong!'
            }
        return JsonResponse(response)


class CreateEducationView(View):
    @method_decorator(login_required)
    def post(self, request):
        if self.request.POST:
            college = request.POST.get('college')
            location = request.POST.get('location')
            user_id = request.POST.get('user_id')

            data = Education.objects.filter(
                user_id=user_id
            )
            cdata = len(data)

            if(cdata > 0):
                upd = Education.objects.get(user_id=user_id)
                upd.college = college
                upd.location = location
                upd.user_id = user_id
                upd.save()
                response = {
                    'success': 'Success!'
                }
            else:
                Education.objects.create(
                    college=college,
                    location=location,
                    user_id=user_id
                                       )
                response = {
                    'success': 'Success!'
                }
        else:
            response = {
                'error': 'something went wrong!'
            }
        return JsonResponse(response)


class GetContactinfoView(View):
    def get(self, request, user_id):
        data = Contact.objects.filter(user_id=user_id).values('username','email', 'mobile','address','website','social_link','birthday','gender','language','interest')
        users_list = list(data)
        return JsonResponse(users_list, safe=False)


class GetDetailsinfoView(View):
    def get(self, request, user_id):
        data = Details.objects.filter(user_id=user_id).values('name', 'about','quote')
        users_list = list(data)
        return JsonResponse(users_list, safe=False)


class GetPlaceinfoView(View):
    def get(self, request, user_id):
        data = Address.objects.filter(user_id=user_id).values('lived', 'current_city')
        users_list = list(data)
        return JsonResponse(users_list, safe=False)


class GetRelationinfoView(View):
    def get(self, request, user_id):
        data = Relation.objects.filter(user_id=user_id).values('status', 'relation')
        users_list = list(data)
        return JsonResponse(users_list, safe=False)


class GetCompanyinfoView(View):
    def get(self, request, user_id):
        data = Work.objects.filter(user_id=user_id).values('company', 'designation')
        users_list = list(data)
        return JsonResponse(users_list, safe=False)


class GetEducationInfoView(View):
    def get(self, request, user_id):
        data = Education.objects.filter(user_id=user_id).values('college', 'location')
        users_list = list(data)
        return JsonResponse(users_list, safe=False)


class CreateProfileImageView(View):
    def post(self, request):
        if self.request.FILES:
            profile = request.FILES['profile']

            data = ProfileImage.objects.filter(user_id=request.user.id)

            datalen = len(data)

            if datalen > 0:
                upd = ProfileImage.objects.get(user_id=request.user.id)
                upd.profile = profile
                upd.user_id = request.user.id
                upd.save()

            else:
                ProfileImage.objects.create(profile=profile, user_id=request.user.id)
            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:
            return JsonResponse({"error": 500}, json_dumps_params={'indent': 2})


class CreateCoverImageView(View):
    def post(self, request):
        if self.request.FILES:
            cover = request.FILES['cover']

            data = ProfileImage.objects.filter(user_id=request.user.id)

            datalen = len(data)

            if datalen > 0:
                upd = ProfileImage.objects.get(user_id=request.user.id)
                upd.cover = cover
                upd.user_id = request.user.id
                upd.save()

            else:
                ProfileImage.objects.create(cover=cover, user_id=request.user.id)

            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:
            return JsonResponse({"error": 500}, json_dumps_params={'indent': 2})


class SearchUserView(View):
    def post(self, request):
        username = request.POST.get('username')
        user_profile = User.objects.filter(username=username)
        user_data = User.objects.filter(username=username).first()

        if user_data:
            data_exist = Following.objects.filter(following_id=user_data.id, user_id=request.user.id).first()
            friends = User.objects.filter(username=username)
            len_friend = len(friends)
            if len_friend > 0:
                context = {
                    'friends': friends
                }
                return render(request, 'profile/friend_search.html', context)
        else:
            data_exist = ''

        group = Group.objects.filter(Q(name__contains=username) | Q(codename__contains=username))

        if(data_exist):
            context = {
                'user_profile': user_profile,
                'data_exist': data_exist
            }
            return render(request, 'profile/search.html', context)
        elif group:
            context = {
                'groups': group,
            }
            return render(request, 'group/search.html', context)
        else:
            return HttpResponse('ok')


class NewsFeedView(View):
    @method_decorator(login_required)
    def get(self, request):
        posts = Post.objects.all().order_by('-id')
        friend = Following.objects.filter(following_id=request.user.id, status=2)
        # data = Contact.objects.get_upcoming_birthdays()
        data2 = []
        for value in friend:
            data2 = Contact.objects.filter(user_id=value.user_id).order_by('-birthday')
        all_events = Events.objects.all()

        context = {
            'posts': posts,
            'birthdays': data2,
            'all_events': all_events
        }
        return render(request, 'profile/news_feed.html', context)


class ProfileImageView(View):
    @method_decorator(login_required)
    def get(self, request):
        images = ProfileImage.objects.filter(user_id=request.user.id)
        context = {
            'images': images
        }
        return render(request, 'profile/profile_images.html', context)


class ProfileImageDeleteView(View):
    @method_decorator(login_required)
    def get(self, request, pk):
        images = ProfileImage.objects.filter(pk=pk)
        images.delete()
        return render(request, 'profile/profile_images.html')


class ProfileVideoDeleteView(View):
    @method_decorator(login_required)
    def get(self, request, pk):
        video = Video.objects.filter(pk=pk)
        video.delete()
        return render(request, 'profile/profile_video.html')


class ProfileVideoView(View):
    @method_decorator(login_required)
    def get(self, request):
        videos = Video.objects.filter(user_id=request.user.id)
        context = {
            'videos': videos
        }
        return render(request, 'profile/profile_video.html', context)


class FriendRequestSendView(View):
    @method_decorator(login_required)
    def post(self, request):
        receiver = request.POST.get('receiver_id')
        data = Following.objects.create(user_id=request.user.id, following_id=receiver, status=1)
        # print(receiver)
        user = User.objects.get(pk=receiver)
        notify.send(request.user, recipient=user, actor=request.user, verb='sent friend request.',
                    nf_type='followed_by_one_user')

        return redirect('user:profile')


class CancelFriendRequestView(View):
    @method_decorator(login_required)
    def get(self, request, pk):
        data = Following.objects.filter(user_id=request.user.id, following_id=pk, status=1)
        data.delete()
        return redirect('user:profile')


class ConfirmFriendRequestView(View):
    @method_decorator(login_required)
    def get(self, request, pk):
        data = Following.objects.get(pk=pk)
        data.status = 2
        data.save()

        user = User.objects.get(pk=data.user_id)
        notify.send(request.user, recipient=user, actor=request.user, verb='accepted your request.',
                    nf_type='followed_by_one_user')

        return redirect('user:profile')


class DeleteFriendRequestView(View):
    @method_decorator(login_required)
    def get(self, request, pk):
        data = Following.objects.filter(pk=pk)
        data.delete()
        return redirect('user:profile')


class UserFriendRequest(View):
    @method_decorator(login_required)
    def get(self, request):
        data = Following.objects.filter(following_id=request.user.id, status=1)
        context = {
            'data': data
        }
        return render(request, 'profile/friend_request_list.html', context)


class UserBirthdayView(View):
    def get(self, request):
        friend = Following.objects.filter(following_id=request.user.id, status=2)
        # data = Contact.objects.get_upcoming_birthdays()
        data2 = []
        for value in friend:
            data2 = Contact.objects.filter(user_id=value.user_id).order_by('-birthday')
        # data3 = Contact.objects.get_birthdays()
        # print(data2)
        return render(request, 'profile/birthday.html', context={'data': data2})


class CalenderView(View):
    def get(self, request):
        return render(request, 'profile/calender.html')


def calendar(request):
    all_events = Events.objects.all()
    context = {
        "events": all_events,
    }
    return render(request,'events/calendar.html',context)


def add_event(request):
    start = request.POST.get("start", None)
    end = request.POST.get("end", None)
    title = request.POST.get("title", None)
    types = request.POST.get("type", None)

    event = Events(name=str(title), start=start, end=end, type=types, user_id=request.user.id)
    event.save()
    return redirect("user:events")


def edit(request, pk):
    event = Events.objects.get(pk=pk)
    context = {
        'event': event
    }
    return render(request, 'events/edit_event.html', context)


def update_event(request):
    start = parser.parse(request.POST.get('start'))
    type = request.POST.get("type", None)
    end = parser.parse(request.POST.get('end'))
    title = request.POST.get("title", None)
    id = request.POST.get("event_id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.type = type
    event.save()
    messages.success(request, 'Form submission successful')
    return render(request, 'events/edit_event.html')


def remove(request, pk):
    id = request.GET.get("id", None)
    event = Events.objects.get(pk=pk)
    event.delete()
    messages.success(request, 'Form submission successful')
    return redirect("user:events")


class WorkRemoveView(View):
    def get(self,request, pk):
        data = Work.objects.get(pk=pk)
        data.delete()
        return redirect('user:profile')


class EducationRemoveView(View):
    def get(self,request, pk):
        data = Education.objects.get(pk=pk)
        data.delete()
        return redirect('user:profile')


class EducationEditView(View):
    def get(self,request, pk):
        data = Education.objects.get(pk=pk)
        context ={
            'data': data
        }
        return render(request, 'edit/education.html', context)


class WorkEditView(View):
    def get(self,request, pk):
        data = Work.objects.get(pk=pk)
        context ={
            'data': data
        }
        return render(request, 'edit/work.html', context)


class AccountSettingView(View):
    def get(self,request):

        return render(request, 'profile/account_setting.html')


class PrivacySettingView(View):
    def get(self,request):

        return render(request, 'profile/privacy_setting.html')



