from django.urls import path
from . import views
app_name = "blog"

urlpatterns = [
    path('blog-list', views.BlogListView.as_view(), name="blog-list"),
    path('create-blog-post', views.BlogCreateView.as_view(), name="create-blog-post"),
    path('read-post/<int:pk>', views.BlogReadView.as_view(), name="read-post"),
]