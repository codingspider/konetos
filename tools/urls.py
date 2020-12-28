from django.urls import path
from . import views
app_name = "tools"

from django.urls import path

from . import views


urlpatterns = [
    path("check/", views.check)
]