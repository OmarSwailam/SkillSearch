from django.shortcuts import render

def index(request):
    return render(request, 'application/index.html')

def profile(request):
    return render(request, 'application/profile.html')