from django.urls import path

from . import views

urlpatterns = [
    path('request_reset_email/', views.request_password_reset_email, name='request_reset_email'),
    path('password_reset/<token>/', views.password_reset_email, name='password_reset_confirm'),
]
