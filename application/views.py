from django.shortcuts import render
from .models import Profile

def index(request):
    profiles = Profile.objects.all()
    context = {
        "profiles": profiles
    }
    return render(request, 'application/index.html', context)

def profile(request):
    return render(request, 'application/profile.html')