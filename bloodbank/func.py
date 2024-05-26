from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User,Group
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
# @csrf_exempt
#User registration
def signup(request):
    pass
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass0 = request.POST.get('pass0')
        pass1 = request.POST.get('pass1')
        
        #creating user
        check_user=User.objects.filter(email=email).first()
        check_username=User.objects.filter(username=username).first()


        if len(username)>10:
            messages.success(request,"Username must be under 10 characters")
            return redirect('home')
        if not username.isalnum():
            messages.success(request,"Username must contains only letters and numbers!!")
            return redirect('home')
        if pass0 != pass1:
            messages.success(request,"Password doesnot match!!")
            return redirect('home')
        
        if check_user:
            messages.success(request,"Email is already registered!!")
            return redirect('home')
        if check_username:
            messages.success(request,"Username is already registered!!")
            return redirect('home')
        else:
            myuser=User.objects.create_user(username, email, pass1, first_name=fname, last_name=lname)
            myuser.save()
            messages.success(request,"Your account is created successfully..")
            return redirect('home')
    else:
        return redirect('home')

#User login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass2')


        
        user = authenticate(request, username=username, password=password)


        check_user=User.objects.filter(username=username).first()
        pro_obj=Profile.objects.filter(user=check_user).first()

        if user is None:
            messages.error(request,"User Does not exist!")
            return redirect('home')
        else:
            if user.is_staff:
                if user is not None:
                    login(request, user)
                    print(user)
                    messages.success(request,"You're successfully logged in!")
                    return redirect('home')
                else:
                    messages.error(request,"Sorry invalid credentials!")
                    return redirect('home')
            else:
                if user is not None:
                    login(request, user)
                    print(user)
                    messages.success(request,"You're successfully logged in!")
                    return redirect('home')
                else:
                    messages.error(request,"Sorry invalid credentials!")
                    return redirect('home')
    else:
        return redirect('home')
    
#User logout  
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return redirect('home')