# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Campaign
from .forms import CampaignForm



def campaign_list(request):
    campaigns = Campaign.objects.filter(provider=request.user.bloodbank)
    return render(request, 'camp/campaign_list.html', {'campaigns': campaigns})

def campaign_detail(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    return render(request, 'camp/campaign_detail.html', {'campaign': campaign})

def campaign_create(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            camp = form.save(commit=False)
            camp.provider = request.user.bloodbank
            form.save()
            return redirect('campaign_list')
    else:
        form = CampaignForm()
    return render(request, 'camp/campaign_form.html', {'form': form})

def campaign_update(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES, instance=campaign)
        if form.is_valid():
            form.save()
            return redirect('campaign_list')
    else:
        form = CampaignForm(instance=campaign)
    return render(request, 'camp/campaign_form.html', {'form': form})

def campaign_delete(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    campaign.delete()
    return redirect('campaign_list')
