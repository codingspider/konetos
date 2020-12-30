from django.urls import path
from . import views
app_name = "advertise"

urlpatterns = [
    path("ads-list", views.AdsViewListView.as_view(), name="ads-list"),
    path("create-campaign", views.AdsCreateView.as_view(), name="create-campaign"),
    path("update-campaign", views.CampaignUpdateView.as_view(), name="update-campaign"),
    path("edit-campaign/<int:pk>", views.CampaignEditView.as_view(), name="edit-campaign"),
    path("delete-campaign/<int:pk>", views.DeleteCampaignView.as_view(), name="delete-campaign"),

]