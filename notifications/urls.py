from django.urls import path
from . import views
app_name = "notification"

urlpatterns = [

    path('send/', views.follow_user),


]