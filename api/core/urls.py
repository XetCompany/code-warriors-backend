from django.urls import path

from . import views


urlpatterns = [
    path('requests/', views.RequestModelViewSet.as_view({'get': 'list'})),
    path('request/more/<int:pk>/', views.RequestModelViewSet.as_view({'get': 'retrieve'})),
    path('request/remove/<int:pk>/', views.delete_request_by_pk),
    path('request/response/<int:pk>/', views.add_response_to_request),
    path('request/end/<int:pk>/', views.end_request),
    path('image/', views.ImageView.as_view()),
    path('image/<int:pk>/', views.ImageView.as_view()),
    path('video/', views.VideoView.as_view()),
    path('video/<int:pk>/', views.VideoView.as_view()),
]