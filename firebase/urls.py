from django.urls import path
from . import views

urlpatterns = [
    path('login_firebase/', views.login_firebase),
    path('', views.home),
    path('firebase_login_save', views.login_firebase_save),
    path('login_success/<str:username>/<str:password>/', views.login_request),



]