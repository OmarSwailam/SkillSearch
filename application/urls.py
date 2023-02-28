from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path("register", views.register_user, name="register"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    # Skill Search
    path(
        "",
        views.HomeView.as_view(),
        name="index",
    ),
    # Profile
    path(
        "profile/<uuid:pk>",
        views.ProfileDetailView.as_view(),
        name="profile-detail",
    ),
    path(
        "profile-settings/<uuid:pk>",
        views.ProfileSettingsUpdateView.as_view(),
        name="profile-settings",
    ),
    # Skills
    path(
        "skill/add",
        views.SkillCreateView.as_view(),
        name="add-skill",
    ),
    path(
        "skill/delete/<uuid:pk>",
        views.SkillDeleteView.as_view(),
        name="delete-skill",
    ),
    # CRUD Projects
    path(
        "project/<uuid:pk>",
        views.ProjectDetailView.as_view(),
        name="project",
    ),
    path(
        "project/add",
        views.ProjectCreateView.as_view(),
        name="add-project",
    ),
    path(
        "project/update/<uuid:pk>",
        views.ProjectUpdateView.as_view(),
        name="update-project",
    ),
    path(
        "project/delete/<uuid:pk>",
        views.ProjectDeleteView.as_view(),
        name="delete-project",
    ),
]
