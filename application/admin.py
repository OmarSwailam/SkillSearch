from django.contrib import admin
from .models import User, Profile, Skill

admin.site.register(User)
admin.site.register(Skill)


class SkillInline(admin.TabularInline):
    model = Skill

class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        SkillInline,
    ]

admin.site.register(Profile, ProfileAdmin)
