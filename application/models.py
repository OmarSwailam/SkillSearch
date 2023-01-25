from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True,)
    username = models.CharField(max_length=200, null=True, blank=True,)
    location = models.CharField(max_length=200, null=True, blank=True,)
    email = models.EmailField(max_length=300, null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(max_length=1024, null=True, blank=True)
    profile_image = models.ImageField(
        null=True, blank=True, default='profiles/user-default.png', upload_to='profiles/')
    github_link = models.SlugField(null=True, blank=True)
    linkedin_link = models.SlugField(null=True, blank=True)
    website_link = models.SlugField(null=True, blank=True)
    twitter_link = models.SlugField(null=True, blank=True)
    youtube_link = models.SlugField(null=True, blank=True)
    social_link = models.SlugField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.username}'


class Skill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.name.capitalize()}'
