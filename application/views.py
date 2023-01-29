from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm, SkillForm


def register_user(request):
    page = 'register'
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.name = user.name.title()
            user.save()
            messages.success(
                request, f'Hey {user.name}, let\'s setup your profile!')

            login(request, user)
            return redirect('profile-settings')
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


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.info(request, 'See you again!')
    return redirect('index')


def index(request):
    profiles = Profile.objects.all()
    return render(request, 'application/index.html', {
        'profiles': profiles
    })

def others_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.user.is_authenticated:
        if profile == request.user.profile:
            return redirect('profile')
    skills = profile.skill_set.all()
    return render(request, 'application/others-profile.html', {
        'profile': profile,
        'skills': skills
    })

def profile(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    return render(request, 'application/profile.html', {
        'profile': profile,
        'skills': skills
    })


@login_required(login_url='login')
def profile_settings(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.name = profile.name.title()
            profile.save()
            return redirect('profile')

    return render(request, 'application/profile-settings.html', {
        'form': ProfileForm(instance=profile)
    })


@login_required(login_url='login')
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = request.user.profile
            skill.save()
            messages.success(request, 'skill added successfully')
            return redirect('profile')
    return render(request, 'application/add-skill.html', {
        'form': SkillForm(),
    })


def delete_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('profile')
    return render(request, 'application/delete-object.html', {
        'object': skill
    })