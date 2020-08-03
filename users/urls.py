from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.u_login, name='login'),
    path('logout/', views.u_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/user/<int:pk>', views.profile_user, name='profile-user'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password-reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password-reset-done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password-reset-confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password-reset-complete'),



    # PasswordResetView
    # PasswordResetDoneView
    # PasswordResetConfirmView
    # PasswordResetCompleteView
]