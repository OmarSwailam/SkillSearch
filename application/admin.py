from django.contrib import admin
from .models import User, Profile, Skill, Project, ProjectImage

admin.site.register(User)
admin.site.register(Skill)


class SkillInline(admin.TabularInline):
    model = Skill


class ProjectInline(admin.StackedInline):
    model = Project


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage


class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        SkillInline,
        ProjectInline,
    ]


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectImageInline,
    ]




admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
