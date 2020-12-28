from django.conf.urls import url
from django.urls import path, include
from . import views
app_name = "friendship"

urlpatterns = [
    path('friendship_add_friend/<int:to_username>', views.AddFriendView.as_view(), name="friendship_add_friend"),
    path('block/<int:to_username>', views.UnfollowFriendView.as_view(), name="block"),
    path('remove/<int:to_username>', views.RemoveFriendView.as_view(), name="remove"),
    path('friend-list', views.FriendListView.as_view(), name="friend-list"),

]