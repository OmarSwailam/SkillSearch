from django.db import models
from django.db.models import Prefetch, Q


class ProfileQuerySet(models.QuerySet):
    def with_skills(self):
        from .models import Skill

        return self.prefetch_related(
            Prefetch("skills", queryset=Skill.objects.all(), to_attr="skills_list")
        )

    def with_projects(self):
        from .models import Project

        return self.prefetch_related(
            Prefetch(
                "projects", queryset=Project.objects.all(), to_attr="projects_list"
            )
        )

    def with_skills_and_projects(self):
        return self.with_skills().with_projects()

    def filter_for_profiles(self, qstring):
        return self.filter(
            Q(name__icontains=qstring)
            | Q(job_title__icontains=qstring)
            | Q(skills__name__icontains=qstring)
        ).distinct()


class ProfileManager(models.Manager.from_queryset(ProfileQuerySet)):
    pass


class ProjectQuerySet(models.QuerySet):
    def get_images(self):
        from .models import ProjectImage

        return self.prefetch_related(
            Prefetch(
                "projectimage_set",
                queryset=ProjectImage.objects.filter(image__isnull=False),
                to_attr="images_list",
            )
        )


class ProjectManager(models.Manager.from_queryset(ProjectQuerySet)):
    pass
