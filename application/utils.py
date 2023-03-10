from .models import Profile, Skill
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProfiles(request, profiles, results):

    page = request.GET.get('page')

    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    left_index = (int(page) - 4) if (int(page) > 4) else 1
    right_index = (int(page) + 5) if (int(page) < paginator.num_pages - 5) else paginator.num_pages + 1
    custom_paginator = range(left_index, right_index)

    return profiles, custom_paginator

def searchProfiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(job_title__icontains=search_query) |
        Q(skill__in=skills))

    return profiles, search_query