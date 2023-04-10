from django.urls import path

from . import views


urlpatterns = [
    path('requests/', views.RequestListOrDetailModelViewSet.as_view({'get': 'list'})),
    path('request/detail/<int:pk>/', views.RequestListOrDetailModelViewSet.as_view({'get': 'retrieve'})),
    path('request/create/', views.RequestCreateOrUpdateModelViewSet.as_view({'post': 'create'})),
    path('request/update/<int:pk>/', views.RequestCreateOrUpdateModelViewSet.as_view({'put': 'update'})),
    path('request/remove/<int:pk>/', views.delete_request_by_pk),

    path('request/response/<int:pk>/', views.add_response_to_request),
    path('request/end/<int:pk>/', views.end_request),

    path('image/', views.ImageView.as_view()),
    path('image/<int:pk>/', views.ImageView.as_view()),

    path('video/', views.VideoView.as_view()),
    path('video/<int:pk>/', views.VideoView.as_view()),

    path('user/detail/<int:pk>/', views.UserDetailModelViewSet.as_view({'get': 'retrieve'})),
    path('user/update/', views.user_info_update),

]