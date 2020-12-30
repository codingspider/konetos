from django.conf.urls import url
from django.urls import path
from . import views
app_name = "user"

urlpatterns = [

    path('profile/', views.ProfileView.as_view(), name="profile"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("contact-information-create", views.ContactInformationView.as_view(), name="contact-information-create"),
    path("detail-information-create", views.DetailInformationView.as_view(), name="detail-information-create"),
    path("get-contact-information/<int:user_id>", views.GetContactinfoView.as_view(), name="get-contact-information"),
    path("get-details-information/<int:user_id>", views.GetDetailsinfoView.as_view(), name="get-details-information"),
    path("place-information-create", views.PlaceCreteView.as_view(), name="place-information-create"),
    path("get-place-information/<int:user_id>", views.GetPlaceinfoView.as_view(), name="get-place-information"),
    path("relation-information-create", views.RelationCreateView.as_view(), name="relation-information-create"),
    path("get-relation-information/<int:user_id>", views.GetRelationinfoView.as_view(), name="get-relation-information"),
    path("work-information-create", views.WorkCreateView.as_view(), name="work-information-create"),
    path("get-company-information/<int:user_id>", views.GetCompanyinfoView.as_view(), name="get-company-information"),
    path("get-education-information/<int:user_id>", views.GetEducationInfoView.as_view(), name="get-education-information"),
    path("education-information-create", views.CreateEducationView.as_view(), name="education-information-create"),
    path("profile-image-create", views.CreateProfileImageView.as_view(), name="profile-image-create"),
    path("cover-image-create", views.CreateCoverImageView.as_view(), name="cover-image-create"),
    path("search", views.SearchUserView.as_view(), name="search"),
    path("news-feed", views.NewsFeedView.as_view(), name="news-feed"),
    path("profile-image", views.ProfileImageView.as_view(), name="profile-image"),
    path("profile-video", views.ProfileVideoView.as_view(), name="profile-video"),
    path("profile-image-delete/<int:pk>", views.ProfileImageDeleteView.as_view(), name="profile-image-delete"),
    path("profile-video-delete/<int:pk>", views.ProfileVideoDeleteView.as_view(), name="profile-video-delete"),
    path('send-friend-request', views.FriendRequestSendView.as_view(), name="send-friend-request"),
    path('user-friend-request', views.UserFriendRequest.as_view(), name="user-friend-request"),
    path('cancel-request/<int:pk>', views.CancelFriendRequestView.as_view(), name="cancel-request"),
    path('delete-request/<int:pk>', views.DeleteFriendRequestView.as_view(), name="delete-request"),
    path('confirm-request/<int:pk>', views.ConfirmFriendRequestView.as_view(), name="confirm-request"),
    path('user-birthday', views.UserBirthdayView.as_view(), name="user-birthday"),
    # path('calender', views.CalenderView.as_view(), name="calender"),

    path('events/', views.calendar, name='events'),
    path('add_event/', views.add_event, name='add_event'),
    path('update_event/', views.update_event, name='update_event'),
    path('edit-event/<int:pk>', views.edit, name='edit-event'),
    path('delete-event/<int:pk>', views.remove, name='delete-event'),

    path('work-remove/<int:pk>', views.WorkRemoveView.as_view(), name="work-remove"),
    path('education-remove/<int:pk>', views.EducationRemoveView.as_view(), name="education-remove"),
    path('education-edit/<int:pk>', views.EducationEditView.as_view(), name="education-edit"),
    path('work-edit/<int:pk>', views.WorkEditView.as_view(), name="work-edit"),

    path("account-setting/", views.AccountSettingView.as_view(), name="account-setting"),
    path("privacy-setting/", views.PrivacySettingView.as_view(), name="privacy-setting"),
    path("update_server/", views.update, name="update"),


]