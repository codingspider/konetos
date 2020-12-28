from comment.models import Comment
from django import template

from post.models import Post

register = template.Library()


@register.simple_tag
def comment_post(user_id):
    follower = Post.objects.get(pk=user_id)
    return follower

