from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CustomUserCreationForm
from .models import Profile, Project, Skill
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)


def register_user(request):
    if not request.user.is_anonymous:
        return redirect("index")
    page = "register"
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.name = user.name.title()
            user.save()
            messages.success(request, f"Hey {user.name}, let's setup your profile!")

            login(request, user)
            return redirect("profile-settings")
        else:
            return render(
                request, "application/login-register.html", {"page": page, "form": form}
            )

    return render(
        request,
        "application/login-register.html",
        {"page": page, "form": CustomUserCreationForm()},
    )


def login_user(request):
    if not request.user.is_anonymous:
        return redirect("index")
    page = "login"
    if request.method == "POST":
        email = request.POST["email"].lower()
        password = request.POST["password"]

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome!")
            return redirect(request.GET["next"] if request.GET.get("next") else "index")
        else:
            messages.error(request, "Wrong Email or/and Password")

    return render(
        request,
        "application/login-register.html",
        {
            "page": page,
        },
    )


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    messages.info(request, "See you again!")
    return redirect("index")


class SuccessURLMixin:
    def get_success_url(self):
        return self.request.user.profile.get_absolute_url()


class HomeView(ListView):
    model = Profile

    template_name = "application/index.html"
    context_object_name = "profiles"
    ordering = ["-id"]
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()

        search_query = self.request.GET.get("search_query", "")
        if search_query:
            queryset = queryset.filter_for_profiles(search_query)
        return queryset


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "application/others-profile.html"
    context_object_name = "profile"

    login_url = "login"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.with_skills_and_projects()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["skills"] = self.object.skills_list
        context["projects"] = self.object.projects_list
        return context


class ProfileSettingsUpdateView(LoginRequiredMixin, SuccessURLMixin, UpdateView):
    template_name = "application/profile-settings.html"
    model = Profile
    fields = [
        "name",
        "location",
        "email",
        "job_title",
        "bio",
        "profile_image",
        "github_link",
        "linkedin_link",
        "website_link",
        "twitter_link",
        "youtube_link",
        "phone_number",
    ]

    login_url = "login"


class SkillCreateView(
    LoginRequiredMixin, SuccessMessageMixin, SuccessURLMixin, CreateView
):
    template_name = "application/add-skill.html"
    model = Skill
    fields = ["name"]
    success_message = "%(name)s was created successfully"

    login_url = "login"

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)


class SkillDeleteView(LoginRequiredMixin, SuccessURLMixin, DeleteView):
    template_name = "application/delete-skill.html"
    model = Skill
    context_object_name = "skill"

    login_url = "login"


class ProjectListView(LoginRequiredMixin, ListView):
    template_name = "application/projects.html"
    model = Project
    context_object_name = "projects"

    login_url = "login"

    def get_queryset(self):
        queryset = super().get_queryset().get_images()
        queryset = queryset.filter(owner=self.request.user.profile)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images"] = self.object.images_list
        return context


class ProjectDetailView(LoginRequiredMixin, DetailView):
    template_name = "application/project-detail.html"
    model = Project
    context_object_name = "project"

    login_url = "login"

    def get_queryset(self):
        queryset = super().get_queryset().get_images()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images"] = self.object.images_list
        return context


class ProjectCreateView(
    LoginRequiredMixin, SuccessMessageMixin, SuccessURLMixin, CreateView
):
    template_name = "application/add-project.html"
    model = Project
    fields = [
        "title",
        "description",
        "image",
        "demo_link",
        "source_link",
    ]
    success_message = "%(title)s was created successfully"

    login_url = "login"

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)


class ProjectDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = "application/project-delete.html"
    model = Project
    context_object_name = "project"

    login_url = "login"


class ProjectUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "application/project-update.html"
    model = Project
    fields = [
        "title",
        "description",
        "image",
        "demo_link",
        "source_link",
    ]
    success_message = "%(title)s was updated successfully"

    login_url = "login"
