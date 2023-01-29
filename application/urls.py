from django.urls import path
from . import views
urlpatterns = [
    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),


    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('profile-settings', views.profile_settings, name='profile-settings'),

    path('add-skill', views.add_skill, name='add-skill'),
    path('delete-skill/<str:pk>', views.delete_skill, name='delete-skill'),
]
