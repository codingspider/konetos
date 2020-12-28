from django.contrib import admin
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from .models import *


class AutoFriendAdmin(admin.ModelAdmin):
    exclude = ('user_id', )


class AutoGroupJoinAdmin(admin.ModelAdmin):
    exclude = ('user_id', )


class AutoPageLikeAdmin(admin.ModelAdmin):
    exclude = ('user_id', )


admin.site.register(AutoFriend, AutoFriendAdmin)
admin.site.register(AutoGroupJoin, AutoGroupJoinAdmin)
admin.site.register(AutoPageLike, AutoPageLikeAdmin)
