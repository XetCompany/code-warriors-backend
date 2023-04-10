from django.urls import path, include

from . import example_views

urlpatterns = [
    path('hello/', example_views.hello),
    path('email/', example_views.send_email),

    path('auth/', include('api.auth.urls')),
]
