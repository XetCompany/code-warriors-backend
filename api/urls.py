from django.urls import path

from . import example_views

urlpatterns = [
    path('hello/', example_views.hello),
    path('email/', example_views.send_email),
]
