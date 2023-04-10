from django.urls import path, include

urlpatterns = [
    path('auth/', include('api.auth.urls')),

    path('info/', include('api.core.urls')),
]
