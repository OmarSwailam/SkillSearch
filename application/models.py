from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_name(self):
        return self.name

    def __str__(self) -> str:
        return self.email


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True, blank=True,)
    email = models.EmailField(max_length=300)
    job_title = models.CharField(max_length=100)
    bio = models.TextField(max_length=1024)
    profile_image = models.ImageField(
        null=True, blank=True, default='profile-default.png', upload_to='profiles/')
    github_link = models.CharField(max_length=2048, null=True, blank=True)
    linkedin_link = models.CharField(max_length=2048, null=True, blank=True)
    website_link = models.CharField(max_length=2048, null=True, blank=True)
    twitter_link = models.CharField(max_length=2048, null=True, blank=True)
    youtube_link = models.CharField(max_length=2048, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.email}'


class Skill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.name.capitalize()}'


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(default='default.png', upload_to='projects/')
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2048, null=True, blank=True)
    source_link = models.CharField(max_length=2048, null=True, blank=True)

    class Meta:
        ordering = ['-created', '-title']

    def __str__(self) -> str:
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return self.project.title
