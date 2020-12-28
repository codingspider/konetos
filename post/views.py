from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.http import HttpResponse, response, JsonResponse
# Create your views here.
from django.views import View
from .models import Post, Video, Reaction, Photo, SavePost, PostComment
from notify.signals import notify

from web.models import Privacy, Terms

from userprofile.models import Education, Work, Contact


class PostCreateView(View):
    def post(self, request):
        if self.request.POST:

            body = request.POST.get('body', None)
            group_id = request.POST.get('id', None)
            if (body):
                instance = Post.objects.create(body=body, user_id=request.user.id, group_id=group_id)
                id = instance.pk
            else:
                return JsonResponse({"error": 500}, json_dumps_params={'indent': 2})
            if self.request.FILES:
                upload = request.FILES.getlist('uploadfile[]')
                uplen = len(upload)
                x = 0
                for each in upload:
                    Photo.objects.create(photo=each, post_id=id, user_id=request.user.id)

                video = request.FILES.get('video', None)
                if video is not None:
                    Video.objects.create(video=video, post_id=id, user_id=request.user.id)
            
            return JsonResponse({"success": 200})

        else:
            return JsonResponse({"error": 500}, json_dumps_params={'indent': 2})


class PostPhotoDeleteView(View):
    def get(self, request, pk):
        data = Photo.objects.get(pk=pk)
        data.delete()
        return redirect('user:profile')


class PostDeleteView(View):
    def get(self, request, pk):
        data = Post.objects.get(pk=pk)
        data.delete()
        return redirect('user:profile')


class PostHideView(View):
    def get(self, request, pk):
        data = Post.objects.get(pk=pk)
        data.status = 2
        data.save()
        return redirect('user:profile')


class UserSavePost(View):
    def get(self, request, pk):
        data = SavePost.objects.create(user_id=request.user.id, post_id=pk)
        return redirect('user:profile')


class PostReactionSaveView(View):
    """docstring for ClassName"""

    def post(self, request):
        like = request.POST.get('like')
        love = request.POST.get('love')
        sad = request.POST.get('sad')
        think = request.POST.get('think')
        happy = request.POST.get('happy')
        haha = request.POST.get('haha')
        lovely = request.POST.get('lovely')

        post_id = request.POST.get('post_id')
        user_id = request.user.id
        check_data = Reaction.objects.filter(post_id=post_id, user_id=user_id)

        len_data = len(check_data)

        if len_data > 0:
            if like:
               
                updated_rows = Reaction.objects.filter(post_id=post_id, user_id=user_id).update(like=like, love=love,Lovely=lovely,happy=happy,sad=sad,haha=haha,think=think)
                data = Post.objects.get(pk=post_id)
                user = User.objects.get(pk=data.user_id)
                notify.send(request.user, recipient=user, actor=request.user, verb='likes your post',
                            nf_type='followed_by_one_user')

                return JsonResponse({"success": 200})

            if love:
               
                updated_rows = Reaction.objects.filter(post_id=post_id, user_id=user_id).update(like=like, love=love,Lovely=lovely,happy=happy,sad=sad,haha=haha,think=think)
                data = Post.objects.get(pk=post_id)
                user = User.objects.get(pk=data.user_id)
                notify.send(request.user, recipient=user, actor=request.user, verb='React love to your post',
                            nf_type='followed_by_one_user')
                return JsonResponse({"success": 200})

            if sad:
                data = Post.objects.get(pk=post_id)
                user = User.objects.get(pk=data.user_id)
                notify.send(request.user, recipient=user, actor=request.user, verb='React sad to your post',
                            nf_type='followed_by_one_user')
                updated_rows = Reaction.objects.filter(post_id=post_id, user_id=user_id).update(like=like, love=love,Lovely=lovely,happy=happy,sad=sad,haha=haha,think=think)
                return JsonResponse({"success": 200})

            if happy:
                data = Post.objects.get(pk=post_id)
                user = User.objects.get(pk=data.user_id)
                notify.send(request.user, recipient=user, actor=request.user, verb='React happy to your post',
                            nf_type='followed_by_one_user')
                updated_rows = Reaction.objects.filter(post_id=post_id, user_id=user_id).update(like=like, love=love,Lovely=lovely,happy=happy,sad=sad,haha=haha,think=think)
                return JsonResponse({"success": 200})

            if haha:
                data = Post.objects.get(pk=post_id)
                user = User.objects.get(pk=data.user_id)
                notify.send(request.user, recipient=user, actor=request.user, verb='React haha to your post',
                            nf_type='followed_by_one_user')
                updated_rows = Reaction.objects.filter(post_id=post_id, user_id=user_id).update(like=like, love=love,Lovely=lovely,happy=happy,sad=sad,haha=haha,think=think)
                return JsonResponse({"success": 200})

            if lovely:
                data = Post.objects.get(pk=post_id)
                user = User.objects.get(pk=data.user_id)
                notify.send(request.user, recipient=user, actor=request.user, verb='React lovely to your post',
                            nf_type='followed_by_one_user')
                updated_rows = Reaction.objects.filter(post_id=post_id, user_id=user_id).update(like=like, love=love,Lovely=lovely,happy=happy,sad=sad,haha=haha,think=think)
                return JsonResponse({"success": 200})

            if think:
                data = Post.objects.get(pk=post_id)
                user = User.objects.get(pk=data.user_id)
                notify.send(request.user, recipient=user, actor=request.user, verb='React think to your post',
                            nf_type='followed_by_one_user')
                updated_rows = Reaction.objects.filter(post_id=post_id, user_id=user_id).update(like=like, love=love,Lovely=lovely,happy=happy,sad=sad,haha=haha,think=think)
                return JsonResponse({"success": 200})
        else:
            if like:
                data = Post.objects.get(pk=post_id)
                user = User.objects.get(pk=data.user_id)
                notify.send(request.user, recipient=user, actor=request.user, verb='React like to your post',
                            nf_type='followed_by_one_user')

                instance = Reaction.objects.create(user_id=user_id, post_id=post_id, like=like, love=love,Lovely=lovely,happy=happy,sad=sad,haha=haha,think=think)
            elif love:
                data = Post.objects.get(pk=post_id)
                user = User.objects.get(pk=data.user_id)
                notify.send(request.user, recipient=user, actor=request.user, verb='React love to your post',
                            nf_type='followed_by_one_user')
                instance = Reaction.objects.create(user_id=user_id, post_id=post_id, like=like, love=love,Lovely=lovely,happy=happy,sad=sad,haha=haha,think=think)
            elif sad:
                data = Post.objects.get(pk=post_id)
                user = User.objects.get(pk=data.user_id)
                notify.send(request.user, recipient=user, actor=request.user, verb='React sad to your post',
                            nf_type='followed_by_one_user')
                instance = Reaction.objects.create(user_id=user_id, post_id=post_id, like=like, love=love,Lovely=lovely,happy=happy,sad=sad,haha=haha,think=think)
            elif haha:
                data = Post.objects.get(pk=post_id)
                user = User.objects.get(pk=data.user_id)
                notify.send(request.user, recipient=user, actor=request.user, verb='React haha to your post',
                            nf_type='followed_by_one_user')
                instance = Reaction.objects.create(user_id=user_id, post_id=post_id, like=like, love=love,Lovely=lovely,happy=happy,sad=sad,haha=haha,think=think)
            elif happy:
                data = Post.objects.get(pk=post_id)
                user = User.objects.get(pk=data.user_id)
                notify.send(request.user, recipient=user, actor=request.user, verb='React happy to your post',
                            nf_type='followed_by_one_user')
                instance = Reaction.objects.create(user_id=user_id, post_id=post_id, like=like, love=love,Lovely=lovely,happy=happy,sad=sad,haha=haha,think=think)
            elif lovely:
                data = Post.objects.get(pk=post_id)
                user = User.objects.get(pk=data.user_id)
                notify.send(request.user, recipient=user, actor=request.user, verb='React lovely to your post',
                            nf_type='followed_by_one_user')
                instance = Reaction.objects.create(user_id=user_id, post_id=post_id, like=like, love=love,Lovely=lovely,happy=happy,sad=sad,haha=haha,think=think)
            elif think:
                data = Post.objects.get(pk=post_id)
                user = User.objects.get(pk=data.user_id)
                notify.send(request.user, recipient=user, actor=request.user, verb='React think to your post',
                            nf_type='followed_by_one_user')
                instance = Reaction.objects.create(user_id=user_id, post_id=post_id, like=like, love=love,Lovely=lovely,happy=happy,sad=sad,haha=haha,think=think)
            return JsonResponse({"success": 200})


class PostShareView(View):
    def get(self, request, pk):
        data = Post.objects.filter(pk=pk)
        post_count = len(data)
        photo = Photo.objects.filter(post_id=pk)
        photo_count = len(photo)
        video = Video.objects.filter(post_id=pk)
        video_count = len(video)

        if post_count > 0:
            post = Post.objects.get(pk=pk)
            Post.objects.create(body=post.body, user_id=request.user.id, status=1)
        if video_count > 0:
            post_video = Video.objects.get(post_id=pk)
            Video.objects.create(video=post_video.video, post_id=pk, user_id=request.user.id)
        if photo_count > 0:
            post_photo = Photo.objects.get(post_id=pk)
            Photo.objects.create(photo=post_photo.photo, post_id=pk, user_id=request.user.id)
        return redirect('user:profile')


class PrivacyListView(View):
    def get(self, request):
        data = Privacy.objects.latest('-id')
        context = {
            'privacy': data
        }
        return render(request, 'page/privacy.html', context)


class TermsListView(View):
    def get(self, request):
        data = Terms.objects.latest('-id')
        context = {
            'terms': data
        }
        return render(request, 'page/terms.html', context)


class UpdateEducationView(View):
    def post(self,request):
        pk = request.POST.get('pk')
        data = Education.objects.get(pk=pk)
        data.college = request.POST.get('college')
        data.location = request.POST.get('location')
        data.save()
        return redirect('user:profile')


class UpdateWorkView(View):
    def post(self,request):
        pk = request.POST.get('pk')
        data = Work.objects.get(pk=pk)
        data.company = request.POST.get('company')
        data.designation = request.POST.get('designation')
        data.save()
        return redirect('user:profile')


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        postsno = request.POST.get("postsno")
        post = Post.objects.get(pk=postsno)
        user = request.user
        receiver = User.objects.filter(id=post.user_id).first()
        parentsno = request.POST.get("parentsno")

        if parentsno == "":

            comments = PostComment(comment=comment, user=user, post=post)
            comments.save()
            if receiver != request.user:
                data = Post.objects.get(pk=post.id)
                user = User.objects.get(pk=data.user_id)
                notify.send(request.user, recipient=user, actor=request.user, verb='commented on your post.', nf_type='followed_by_one_user')

            messages.success(request, 'Success! your comment have been posted successfully.')
        else:
            parent = PostComment.objects.get(pk=parentsno)
            comments = PostComment(comment=comment, user=user, post=post, parent=parent)
            comments.save()
            receiver2 = parent.user

            if receiver != receiver2 and receiver != request.user:
                notify.send(user, recipient=receiver,
                            verb=" has replied  on someones comment in your post" + f''' <a class =" btn btn-primary btn-sm " href="/posts/post/{post.id}">go</a> ''')
            if receiver2 != request.user:
                notify.send(user, recipient=receiver2,
                            verb=" has replied to your comment" + f''' <a class =" btn btn-primary btn-sm " href="/posts/post/{post.id}">go</a> ''')
            messages.success(request, 'Success! your reply have been posted successfully.')
            return redirect("user:profile")
    return redirect("user:profile")


def deletecomment(request):
    if request.method == "POST":
        parentsno = request.POST.get("parentsno")
        comment = PostComment.objects.get(pk=parentsno)
        postsno = request.POST.get("postsno")
        post = Post.objects.get(pk=postsno)
        if request.user == comment.user:
            comment.delete()
        else:
            raise PermissionDenied
    messages.success(request, 'Successfully Deleted Your Comment')
    return redirect("user:profile")