from django.urls import path

from . import views


urlpatterns = [
    path('requests/', views.RequestModelViewSet.as_view({'get': 'list'})),
    path('request/more/<int:pk>/', views.RequestModelViewSet.as_view({'get': 'retrieve'})),
    path('request/response/<int:pk>/', views.add_response_to_request),
]