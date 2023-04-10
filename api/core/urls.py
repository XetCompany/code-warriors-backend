from django.urls import path

from . import views


urlpatterns = [
    path('requests/', views.RequestModelViewSet.as_view({'get': 'list'})),
    path('request/response/<int:pk>/', views.add_response_to_request),
]