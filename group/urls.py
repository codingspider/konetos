from django.conf.urls import url
from django.urls import path, include
from . import views
app_name = "group"

urlpatterns = [
    path('list/', views.GroupListView.as_view(), name="list"),
    path('user-save-to-group/', views.GroupMemberCreateView.as_view(), name="user-save-to-group"),
    path('create-group/', views.CreateGroupView.as_view(), name="create-group"),
    path('manage-group/<int:pk>', views.ManageGroupView.as_view(), name="manage-group"),
    path('group-members/<int:pk>', views.GroupMemberView.as_view(), name="group-members"),
    path('group-setting/<int:pk>', views.SettingGroupView.as_view(), name="group-setting"),
    path("group-profile-image-create", views.GroupProfileImageView.as_view(), name="group-profile-image-create"),
    path("group-cover-image-create", views.GroupCoverImageCreate.as_view(), name="group-cover-image-create"),


]