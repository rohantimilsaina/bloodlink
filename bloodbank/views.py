from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from .models import Blood, Campaign,BloodBank
from .forms import BloodForm, CampaignForm, BloodBankForm, BloodBankUpdateForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
import logging

def home(request):
    return render(request, 'home.html')


def blood_create(request):
    if request.method == 'POST':
        form = BloodForm(request.POST)
        if form.is_valid():
            blood = form.save(commit=False)
            blood.provider = request.user.bloodbank
            form.save()
            return redirect('blood_list')  # Redirect to the list view after successful creation
    else:
        form = BloodForm()
    return render(request, 'blood_create.html', {'form': form})


def blood_list(request):
    blood = Blood.objects.filter(provider=request.user.bloodbank)
    return render(request, 'blood_list.html', {'blood': blood})
    # return HttpResponse('You dont have any blood records...........')

def blood_update(request, pk):
    instance = get_object_or_404(Blood, pk=pk)
    form = BloodForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('blood_list')
    return render(request, 'blood_create.html', {'form': form})

def blood_delete(request, pk):
    instance = get_object_or_404(Blood, pk=pk)
    instance.delete()
    return redirect('blood_list')





@login_required
def provider_profile_create(request):
    if request.method == 'POST':
        form = BloodBankForm(request.POST)
        if form.is_valid():
            blood_bank = form.save(commit=False)
            blood_bank.user = request.user
            
            # Retrieve latitude and longitude values as floats
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            
            # Ensure latitude and longitude are not empty strings before converting to floats
            if latitude and longitude:
                blood_bank.latitude = float(latitude)
                blood_bank.longitude = float(longitude)
            else:
                # Handle case where latitude or longitude is missing
                # You can display an error message or take appropriate action
                pass
            
            blood_bank.save()
            
            # Redirect to a success page or return a response
            return redirect('home')  # Replace 'success_url' with the URL name of your success page
    else:
        form = BloodBankForm()
    return render(request, 'update_provider.html', {'form': form})

@login_required
def provider_profile(request):
    bb=BloodBank.objects.get(user=request.user)
    context={"bb":bb}
    return render(request,"provider_profile.html",context)

def provider_profile_for_user(request,id):
    provider = BloodBank.objects.get(id=id)
    context={"provider":provider}
    return render(request,"profile/provider_profile_detail.html",context)

def BloodAndCamp(request):
    # Querying the Campaign objects ordered by publication date (assuming there's a publication_date field)
    campaigns = Campaign.objects.order_by('-created_at')
    
    # Splitting the campaigns into the recent post and other posts
    if campaigns:
        recent_post = campaigns[0]  # Get the most recent post
        other_posts = campaigns[1:4]  # Get the next 3 posts after the recent post
        remaining_posts = campaigns[4:]  # Get the rest of the posts
        
        context = {
            "recent_post": recent_post,
            "other_posts": other_posts,
            "remaining_posts": remaining_posts,
        }
    else:
        context = {
            "campaigns": campaigns,
        }
    
    return render(request, "home.html", context)


def about_us(request):
    return render(request, 'about_us.html')

@login_required
def update_profile_bloodbank(request, id):
    blood_bank = get_object_or_404(BloodBank, id=id, user=request.user)
    
    if request.method == 'POST':
        form = BloodBankForm(request.POST, instance=blood_bank)
        if form.is_valid():
            blood_bank = form.save(commit=False)
            
            # Retrieve latitude and longitude values as floats
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            
            # Ensure latitude and longitude are not empty strings before converting to floats
            if latitude and longitude:
                blood_bank.latitude = float(latitude)
                blood_bank.longitude = float(longitude)
            
            blood_bank.save()
            return redirect('home')  # Replace 'success_url' with the URL name of your success page
    else:
        form = BloodBankForm(instance=blood_bank)
    return render(request, 'blood_bank_update_form.html', {'form': form})


def terms_and_conditions(request):
    return render(request, 'terms.html')

def privacy_concern(request):
    return render(request, 'privacy_concern.html')


import logging
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm  # Import your ContactForm from forms.py

logger = logging.getLogger(__name__)

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                # Send email
                send_mail(
                    'Contact Us Form Submission',
                    f'Name: {name}\nEmail: {email}\nMessage: {message}',
                    email,  # Use the email provided by the user as the sender
                    [settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                logger.info('Contact form email sent successfully')
            except Exception as e:
                logger.error(f'Error sending contact form email: {e}')

            # Redirect to home page after successful submission
            return redirect('home')  # Assuming 'home' is the name of the URL pattern for the home page
    else:
        form = ContactForm()

    return render(request, 'contact_us.html', {'form': form})
