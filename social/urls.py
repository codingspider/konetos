"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
# from django_private_chat import urls as django_private_chat_urls
from django.conf.urls.static import static
from django.conf import settings
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('firebase.urls')),
    path('user/', include('userprofile.urls')),
    path('post/', include('post.urls')),
    # url(r'^', include(django_private_chat_urls)),
    url('friendship/', include('userfollow.urls')),
    path('comment/', include('comment.urls')),
    path('group/', include('group.urls')),
    path('product/', include('marketplace.urls')),
    path('web/', include('web.urls')),
    path('blog/', include('blog.urls')),
    path('todo/', include('todo.urls')),
    url(r'^notifications/', include('notify.urls', 'notifications')),
    url('notification/', include('notifications.urls', 'notifications')),
    url('chat/', include('chat.urls')),
    url('advertise/', include('advertise.urls')),
    url('tools/', include('tools.urls')),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),
    path('channel/', include('chanel.urls')),


]
if urlpatterns:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
