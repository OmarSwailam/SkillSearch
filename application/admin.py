from django.contrib import admin
from .models import User, Profile, Skill, Project


from .models import User, Profile, Skill, Project, ProjectImage


class SkillInline(admin.TabularInline):
    model = Skill


class ProjectInline(admin.StackedInline):
    model = Project


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "last_login",
        "is_superuser",
        "email",
        "name",
        "id",
        "is_active",
        "is_staff",
        "date_joined",
        "password",
    )
    list_filter = (
        "last_login",
        "is_superuser",
        "is_active",
        "is_staff",
        "date_joined",
    )
    raw_id_fields = ("groups", "user_permissions")
    search_fields = ("name",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "created",
        "updated",
        "is_deleted",
        "github_link",
        "linkedin_link",
        "website_link",
        "twitter_link",
        "youtube_link",
        "bio",
        "email",
        "job_title",
        "location",
        "profile_image",
        "phone_number",
        "name",
        "user",
        "id",
    )
    list_filter = ("created", "updated", "is_deleted", "user")
    search_fields = ("name",)
    inlines = [
        SkillInline,
        ProjectInline,
    ]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "created",
        "updated",
        "is_deleted",
        "id",
    )
    list_filter = ("created", "updated", "is_deleted", "owner")
    search_fields = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "owner",
        "source_link",
        "created",
        "updated",
        "is_deleted",
        "image",
        "description",
        "demo_link",
        "id",
    )
    list_filter = ("created", "updated", "is_deleted", "owner")


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "image",
        "id",
    )
    list_filter = ("project",)
