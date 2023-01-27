from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm



def register_user(request):
    page = 'register'
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'User were created successfully')

            login(request, user)
            return redirect('index')
        else:
            return render(request, 'application/login-register.html', {
                'page': page,
                'form': form
            })

    return render(request, 'application/login-register.html', {
        'page': page,
        'form': CustomUserCreationForm()
    })


def login_user(request):
    page = 'login'
    if request.method == 'POST':
        email = request.POST['email'].lower()
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, 'Welcome!')
            return redirect(request.GET['next'] if request.GET.get('next') else 'index')
        else:
            messages.error(request, 'Wrong Email or/and Password')

    return render(request, 'application/login-register.html', {
        'page': page,
    })


@login_required()
def logout_user(request):
    logout(request)
    messages.info(request, 'See you again!')
    return redirect('index')


def index(request):
    profiles = Profile.objects.all()
    return render(request, 'application/index.html', {
        'profiles': profiles
    })


def profile(request):
    return render(request, 'application/profile.html')
