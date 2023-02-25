from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='application/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='application/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='application/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='application/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('others-profile/<str:pk>', views.others_profile, name='others-profile'),
    path('profile-settings', views.profile_settings, name='profile-settings'),

    path('add-skill', views.add_skill, name='add-skill'),
    path('delete-skill/<str:pk>', views.delete_skill, name='delete-skill'),

    path('project/<str:pk>', views.project, name='project'),
    path('add-project', views.add_project, name='add-project'),
    path('update-project/<str:pk>', views.update_project, name='update-project'),
    path('delete-project/<str:pk>', views.delete_project, name='delete-project'),
]
