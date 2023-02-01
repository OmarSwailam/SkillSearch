from django.contrib import admin
from .models import User, Profile, Skill, Project

admin.site.register(User)
admin.site.register(Skill)
admin.site.register(Project)


class SkillInline(admin.TabularInline):
    model = Skill


class ProjectInline(admin.StackedInline):
    model = Project




class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        SkillInline,
        ProjectInline,
    ]




admin.site.register(Profile, ProfileAdmin)
