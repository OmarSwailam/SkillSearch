from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}


def login_user(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, 'Welcome!')
            return redirect(request.GET['next'] if request.GET.get('next') else 'index')
        else:
            messages.error(request, 'Wrong Username or/and Password')

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
    context = {
        "profiles": profiles
    }
    return render(request, 'application/index.html', context)


def profile(request):
    return render(request, 'application/profile.html')
