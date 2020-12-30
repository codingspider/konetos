from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from chanel.models import Channel
from django.views.generic import UpdateView, DeleteView

from .models import Country, Campaign
from .forms import CampaignForm


class AdsViewListView(View):
    def get(self, request):
        campaign = Campaign.objects.filter(user=request.user)
        context = {
            'campaigns': campaign
        }
        return render(request, 'ads/list.html', context)


class AdsCreateView(View):
    def get(self, request):
        channel = Channel.objects.filter(user_id=request.user.id)
        form = CampaignForm()
        county = Country.objects.all()
        context = {
            'channel': channel,
            'countries': county,
            'form': form
        }

        return render(request, 'ads/create.html', context)

    def post(self, request):
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = self.request.user
            obj.image = form.cleaned_data['image']
            obj.save()
            context = {
                'form': form
            }
            messages.success(request, 'Form submission successful')
            return render(request, 'ads/create.html', context)
        else:
            messages.error(request, "Error")

        context = {
            'form': form
        }
        return render(request, 'ads/create.html', context)


class CampaignEditView(View):
    def get(self, request, pk):
        data = Campaign.objects.get(pk=pk)
        form = CampaignForm()
        county = Country.objects.all()
        context = {
            'form': form,
            'data': data,
            'countries': county,
        }
        return render(request, 'ads/update.html', context)


class CampaignUpdateView(View):
    def get(self, request, pk):
        title =request.POST.get('title')
        gender =request.POST.get('gender')
        placement =request.POST.get('placement')
        bidding =request.POST.get('bidding')
        url =request.POST.get('url')
        page =request.POST.get('page')
        audience =request.POST.get('audience')
        start =request.POST.get('start')
        end =request.POST.get('end')
        budget =request.POST.get('budget')
        company =request.POST.get('company')
        description =request.POST.get('description')
        image =request.POST.get('image')

        data = Campaign.objects.get(pk=pk)
        data.tile = title
        data.gender = gender
        data.placement = placement
        data.bidding = bidding
        data.url = url
        data.page = page
        data.audience = audience
        data.start = start
        data.end = end
        data.budget = budget
        data.company = company
        data.description = description
        data.image = image
        data.save()

        return redirect('advertise:ads-list')


class DeleteCampaignView(View):
    def get(self, request, pk):
        data = Campaign.objects.get(pk=pk)
        data.delete()
        return reverse_lazy('advertise:ads-list')
