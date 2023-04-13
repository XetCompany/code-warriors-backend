from django.urls import path

from . import views

urlpatterns = [
    path('chats/', views.get_chats),
    path('messages/<int:user_id>/', views.get_messages),
    path('messages/<int:user_id>/create/', views.send_message),
]