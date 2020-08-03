from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import CreateUserForm, login_form, UserUpdateForm, UserUpdateProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, 'Your account is created '+username)
            return redirect('blog-home')
    else:
        form = CreateUserForm()
    context = {'form':form}
    return render(request, 'users/register.html', context)

def u_login(request):
    user_login = login_form()
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        user_login = authenticate(username = username, password = pwd)
        if user_login is not None:
        #if user_login.is_authenticated:
            login(request, user_login)
            messages.info(request, 'Welcome ! '+ username)
            return redirect('blog-home')
        else:
            messages.info(request, 'Username or password is incorrect')
            user_login = login_form()
    context = {'form':user_login}
    return render(request, 'users/login.html', context) 
    

def u_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    if request.method == "POST":              
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserUpdateProfile(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            u_name = u_form.cleaned_data['username']
            messages.success(request, f'Hi, {u_name} Your account is updated')
            return redirect('blog-home')
    else:
        u_form = UserUpdateForm( instance=request.user)
        p_form = UserUpdateProfile(instance=request.user.profile)
        
    
    context = {'u_form':u_form, 'p_form':p_form}
    return render(request, 'users/profile.html', context)

def profile_user(request, pk):
    user = User.objects.get(id=pk)
    context = {'user':user}

    return render(request, 'users/profile_display.html',context)
