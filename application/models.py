import uuid

from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

from .managers import ProfileManager, ProjectManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address.")
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


class User(PermissionsMixin, AbstractBaseUser):
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def get_name(self):
        return self.name

    def __str__(self) -> str:
        return self.email


class BaseAbstractModel(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        """soft  delete a model instance"""
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True
        ordering = ["-created"]


class SocialLinks(models.Model):
    github_link = models.CharField(max_length=2048, null=True, blank=True)
    linkedin_link = models.CharField(max_length=2048, null=True, blank=True)
    website_link = models.CharField(max_length=2048, null=True, blank=True)
    twitter_link = models.CharField(max_length=2048, null=True, blank=True)
    youtube_link = models.CharField(max_length=2048, null=True, blank=True)

    class Meta:
        abstract = True


class ProfileInfo(models.Model):
    bio = models.TextField(max_length=1024)
    email = models.EmailField(max_length=300)
    job_title = models.CharField(max_length=100)
    location = models.CharField(max_length=200, null=True, blank=True)
    profile_image = models.ImageField(
        null=True, blank=True, default="profile-default.png", upload_to="profiles"
    )
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        abstract = True


class Profile(BaseAbstractModel, ProfileInfo, SocialLinks):
    name = models.CharField(max_length=200)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    objects = ProfileManager()

    def get_absolute_url(self):
        return reverse("profile-detail", kwargs={"pk": self.id})

    def __str__(self) -> str:
        return f"{self.email}"


class Skill(BaseAbstractModel):
    # TODO: add skill level
    name = models.CharField(max_length=64)

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="skills",
    )

    def get_absolute_url(self):
        return reverse("skill-detail", kwargs={"pk": self.id})

    def __str__(self) -> str:
        return f"{self.name.capitalize()}"


class Project(BaseAbstractModel):
    title = models.CharField(max_length=200)
    image = models.ImageField(default="default.png", upload_to="projects")
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2048, null=True, blank=True)
    source_link = models.CharField(max_length=2048, null=True, blank=True)

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    objects = ProjectManager()

    class Meta:
        ordering = ["-created", "-title"]

    def __str__(self) -> str:
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")

    def __str__(self) -> str:
        return self.project.title
