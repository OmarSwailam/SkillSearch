from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (CustomUserCreationForm,
                    ProfileForm, SkillForm, ProjectForm)
from .models import Profile, Project
from .utils import searchProfiles, paginateProfiles


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
            messages.success(request, 'Welcome!')
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
    profiles, search_query = searchProfiles(request)
    profiles, custom_paginator = paginateProfiles(request, profiles, 6)
    return render(request, 'application/index.html', {
        'profiles': profiles,
        'search_query': search_query,
        'custom_paginator': custom_paginator
    })


def others_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.user.is_authenticated:
        if profile == request.user.profile:
            return redirect('profile')
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    return render(request, 'application/others-profile.html', {
        'profile': profile,
        'skills': skills,
        'projects': projects
    })


def profile(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    return render(request, 'application/profile.html', {
        'profile': profile,
        'skills': skills,
        'projects': projects,
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


@login_required(login_url='login')
def delete_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.info(request, 'Skill deleted')
        return redirect('profile')
    return render(request, 'application/delete-object.html', {
        'object': skill
    })


def project(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'application/project.html', {
        'project': project
    })


@login_required(login_url='login')
def add_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user.profile
            form.save()
            messages.success(request, 'Project Uploaded Successfully')
            return redirect(request.GET['next'] if request.GET.get('next') else 'profile')
        else:
            form = ProjectForm(request.POST)
            return redirect(request.GET['next'] if request.GET.get('next') else 'index')

    return render(request, 'application/project-form.html', {
        'form': form,
    })


@login_required(login_url='login')
def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES,instance=project)
        if form.is_valid():
            form = form.save()
            messages.success(request, 'Project Uploaded Successfully')
            return redirect('project', pk)
        else:
            form = ProjectForm(request.POST)
            return redirect('project', pk)
    return render(request, 'application/project-form.html', {
        'form': form,
    })


@login_required(login_url='login')
def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.info(request, 'Project deleted')
        return redirect('profile')
    return render(request, 'application/delete-object.html', {
        'object': project
    })