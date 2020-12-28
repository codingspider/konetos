from django import template
from django.db.models import Count
from post.models import Following
register = template.Library()


@register.simple_tag
def any_function(pk):
    follower = Following.objects.filter(following_id=pk).aggregate(total_follower=Count('id'))
    return {'follower': follower}