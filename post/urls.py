from django.urls import path
from . import views
app_name = "post"

urlpatterns = [

    path('post-create/', views.PostCreateView.as_view(), name="post-create"),
    path("photo-delete/<int:pk>", views.PostPhotoDeleteView.as_view(), name="photo-delete"),
    path("post-delete/<int:pk>", views.PostDeleteView.as_view(), name="post-delete"),
    path("post-save/<int:pk>", views.UserSavePost.as_view(), name="post-save"),
    path("post-hide/<int:pk>", views.PostHideView.as_view(), name="post-hide"),
    path("save-like", views.PostReactionSaveView.as_view(), name="save-like"),
    path("save-love", views.PostReactionSaveView.as_view(), name="save-love"),
    path("save-sad", views.PostReactionSaveView.as_view(), name="save-sad"),
    path("save-happy", views.PostReactionSaveView.as_view(), name="save-happy"),
    path("save-lovely", views.PostReactionSaveView.as_view(), name="save-lovely"),
    path("save-think", views.PostReactionSaveView.as_view(), name="save-think"),
    path("save-haha", views.PostReactionSaveView.as_view(), name="save-haha"),
    path("share-on-your-timeline/<int:pk>", views.PostShareView.as_view(), name="share-on-your-timeline"),
    path("privacy", views.PrivacyListView.as_view(), name="privacy"),
    path("terms", views.TermsListView.as_view(), name="terms"),
    path('education-update/', views.UpdateEducationView.as_view(), name="education-update"),
    path('work-update/', views.UpdateWorkView.as_view(), name="work-update"),
    path('post-comment/', views.postComment, name='post-comment'),


]