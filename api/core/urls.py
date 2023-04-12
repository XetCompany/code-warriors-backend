from django.urls import path

from . import views

urlpatterns = [
    path('requests/', views.RequestListOrDetailModelViewSet.as_view({'get': 'list'})),
    path('requests/<int:user_id>/', views.get_requests_by_user_id),
    path('request/detail/<int:pk>/', views.RequestListOrDetailModelViewSet.as_view({'get': 'retrieve'})),
    path('request/create/', views.RequestCreateOrUpdateModelViewSet.as_view({'post': 'create'})),
    path('request/update/<int:pk>/', views.RequestCreateOrUpdateModelViewSet.as_view({'put': 'update'})),
    path('request/remove/<int:pk>/', views.delete_request_by_pk),

    path('categories/', views.get_categories),

    path('request/<int:pk>/add_response/', views.add_response_to_request),
    path('request/end/<int:pk>/', views.end_request),
    path('request/category/', views.get_requests_by_category),

    path('image/', views.ImageView.as_view()),
    path('image/<int:pk>/', views.ImageView.as_view()),

    path('video/', views.VideoView.as_view()),
    path('video/<int:pk>/', views.VideoView.as_view()),

    path('user/', views.user_info),

    path('notifications/', views.get_user_notifications),
    path('notifications/read_all/', views.read_all_notifications),

    path('rating/', views.rating_of_users),

    path('reviews/list/<int:user_id>/', views.ReviewListAPIView.as_view(), name='review-list'),
    path('reviews/create/', views.ReviewCreateAPIView.as_view(), name='review-create'),
    path('reviews/<int:id>/', views.ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail'),
]
