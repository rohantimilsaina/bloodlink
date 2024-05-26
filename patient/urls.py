# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('chat/<int:receiver_id>/', views.chat_room, name='chat_room'),
    path('send_message/', views.send_message, name='send_message'),
    path('view_users_with_messages/', views.view_users_with_messages, name='view_users_with_messages'),
]
