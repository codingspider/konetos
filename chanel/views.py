from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import ChannelForm
from .models import Channel, ChannelThumbnail


class ChannelListView(View):
    def get(self, request):
        channels = Channel.objects.filter(user_id=request.user.id)
        context = {
            'channels': channels
        }
        return render(request, 'channel/list.html', context)


class ChannelChannelManageView(View):
    def get(self, request, pk):
        channels = Channel.objects.get(pk=pk)
        context = {
            'channel': channels
        }
        return render(request, 'channel/manage.html', context)


class ChannelCreateView(View):
    def post(self, request):
        form = ChannelForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = request.user.id
            obj.profile = form.cleaned_data['profile']
            obj.cover = form.cleaned_data['cover']
            obj.save()
            return redirect('channel:channel-list')
        return render(request, 'channel/create.html', {'form': form})

    def get(self, request):
        form = ChannelForm()
        return render(request, 'channel/create.html', {'form': form})


class ChannelThumbnailEditView(View):
    def post(self, request):
        if self.request.FILES:
            thumbnail = request.FILES['thumbnail']
            channel_id = request.POST.get('channel_id')

            upd = Channel.objects.get(pk=channel_id)
            upd.profile = thumbnail
            upd.save()
            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:

            return JsonResponse({"error": 500})


class ChannelThCoverEditView(View):
    def post(self, request):
        if self.request.FILES:
            cover = request.FILES['cover']
            channel_id = request.POST.get('channel_id')

            upd = Channel.objects.get(pk=channel_id)
            upd.cover = cover
            upd.save()
            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:

            return JsonResponse({"error": 500})

