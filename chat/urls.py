from django.urls import path
from . import views
app_name = "chat"

urlpatterns = [

    path('chat', views.ChatListView.as_view(), name="chat"),

]