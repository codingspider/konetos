
from django import template
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import request
from post.models import Following
from userprofile.models import  ProfileImage
from django.shortcuts import get_object_or_404
from post.models import Reaction, Photo, Video, Post, PostComment
from groups_manager.models import Group, Member, GroupMember
from userprofile.models import Contact
from blog.models import Blog
register = template.Library()


@register.simple_tag
def calc_review_count(user_id):
    follower = Following.objects.filter(following_id=user_id, status=2).count()
    return follower



@register.simple_tag
def user_image(user_id):

    try:
        data= ProfileImage.objects.get(user_id=user_id)
        val = data.profile
        return val
    except ProfileImage.DoesNotExist:
        return False


@register.simple_tag
def user_name(user_id):
    try:
        data = User.objects.get(pk=user_id)
        val = data.username
        return val
    except User.DoesNotExist:
        return None


@register.simple_tag
def rection_get(post_id, userid):
    try:
        data = Reaction.objects.get(user_id=userid, post_id=post_id)
        return data
    except Reaction.DoesNotExist:
        return False


@register.simple_tag
def count_reaction(post_id):
    data = Reaction.objects.filter(post_id=post_id).count()
    return data


@register.simple_tag
def count_group_member(group_id):
    data = GroupMember.objects.filter(group_id=group_id).count()
    return data


@register.simple_tag
def count_group_post(group_id):
    data = Post.objects.filter(group_id=group_id).count()
    return data


@register.simple_tag
def seller_user_name(user_id):
    data = User.objects.get(pk=user_id)
    user = data.username
    return user


@register.simple_tag
def post_photo(post_id):
    data = Photo.objects.filter(post_id=post_id)

    photo = None
    for val in data:
        photo = val.photo
    return photo


@register.simple_tag
def post_video(post_id):
    data = Video.objects.filter(post_id=post_id)

    video = None
    for val in data:
        video = val.video
    return video


@register.simple_tag
def group_user_name(member_id):
    try:
        data = Member.objects.get(pk=member_id)
        return data.username
    except Member.DoesNotExist:
        return False


@register.simple_tag
def friend_find(friend_id, user_id):
    try:
        data = Following.objects.get(user_id=user_id, following_id=friend_id)
        status = data.status
        return status
    except Following.DoesNotExist:
        status = 'NoData'
        return status


@register.simple_tag
def people_like_blog(blog_id):
    try:
        data = Blog.objects.get(pk=blog_id)
        count = data.likes
        return count
    except Blog.DoesNotExist:
        count = 0
        return count



@register.simple_tag
def people_visit_blog(blog_id):
    try:
        data = Blog.objects.get(pk=blog_id)
        count = data.visit
        return count
    except Blog.DoesNotExist:
        count = 0
        return count


@register.simple_tag
def get_all_friend_req(user_id):
    try:
        data = Following.objects.get(following_id=user_id)
        return data
    except Following.DoesNotExist:
        return False


@register.simple_tag
def post_reaction(post_id):
    try:
        data = Reaction.objects.filter(post_id=post_id)
        value = []

        for val in data:
            value = User.objects.filter(pk=val.user_id)
        return value
    except Reaction.DoesNotExist:
        user = []
        context = {
            'data': user
        }
        return context


@register.simple_tag
def post_comment(post_id):
    data = Reaction.objects.filter(post_id=post_id)
    value = []

    for val in data:
        value = User.objects.filter(pk=val.user_id)
    return value


@register.filter(name='get_val')
def get_val(dict, key):
    return dict.get(key)


@register.simple_tag
def get_post_comments(post_id):
    comments = PostComment.objects.filter()
    return {'comments': comments}


