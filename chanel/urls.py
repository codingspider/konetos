from django.conf.urls import url
from django.urls import path

from . import views
app_name = "channel"

urlpatterns = [
    path('channel-list/', views.ChannelListView.as_view(), name="channel-list"),
    path('channel-create/', views.ChannelCreateView.as_view(), name="channel-create"),
    path('channel-thumbnail-create/', views.ChannelThumbnailEditView.as_view(), name="channel-thumbnail-create"),
    path('channel-cover-create/', views.ChannelThCoverEditView.as_view(), name="channel-cover-create"),
    path('manage-channel/<int:pk>', views.ChannelChannelManageView.as_view(), name="manage-channel"),
]