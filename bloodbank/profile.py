from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from .models import Profile,Blood, BloodBank
from .forms import ProfileForm, BloodBankForm
from math import radians, sin, cos, sqrt, atan2
from django.shortcuts import render

@login_required
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            
            # Retrieve latitude and longitude values as floats
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            
            # Ensure latitude and longitude are not empty strings before converting to floats
            if latitude and longitude:
                profile.latitude = float(latitude)
                profile.longitude = float(longitude)
            else:
                # Handle case where latitude or longitude is missing
                return HttpResponse("Latitude and longitude are required.", status=400)            
            profile.save()
            
            # Redirect to a success page
            return redirect('home')  
    else:
        form = ProfileForm()
    return render(request, 'profile/user_update_profile.html', {'form': form})

@login_required
def user_profile(request):
    bb=Profile.objects.get(user=request.user)
    context={"bb":bb}
    return render(request,"profile/user_profile.html",context)

#Calculating distance 
def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two coordinates in kilometers.
    """
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = round(6371 * c, 2)  # Radius of Earth in kilometers
    return distance

def get_blood_data(request, blood_queryset):
    """
    Get blood data and calculate distances.
    """
    user = request.user
    profile = Profile.objects.get(user=user)
    temp = []

    for blood in blood_queryset:
        distance = calculate_distance(
            blood.provider.latitude, 
            blood.provider.longitude, 
            profile.latitude, 
            profile.longitude
        )
        temp.append({'blood': blood, 'distance': distance})

    temp = sorted(temp, key=lambda x: x['distance'])
    return temp

def view_availablity(request):
    """
    View blood availability.
    """
    bloods = Blood.objects.all()
    temp = get_blood_data(request, bloods)
    context = {"my_data": temp}
    return render(request, "profile/bloods.html", context)

def blood_search(request):
    """
    Search for blood availability.
    """
    blood_type = request.GET.get('blood_type')
    if blood_type:
        bloods = Blood.objects.filter(name__icontains=blood_type)
    else:
        bloods = Blood.objects.all()

    temp = get_blood_data(request, bloods)
    context = {"my_data": temp}
    return render(request, "profile/bloods.html", context)


@login_required
def update_profile_user(request, id):
    blood_bank = get_object_or_404(Profile, id=id, user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=blood_bank)
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
            return redirect('user_profile') 
    else:
        form = ProfileForm(instance=blood_bank)
    return render(request, 'profile/profile_update_user.html', {'form': form})
