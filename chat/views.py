from django.shortcuts import render
from django.views import View

from post.models import Following


class ChatListView(View):
    def get(self, request):
        data = Following.objects.filter(following_id=request.user.id, status=2)
        context = {
            'data': data
        }
        return render(request, 'chat/chat.html', context)