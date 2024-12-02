from django.urls import path
from . import views

urlpatterns = [
    path('chat/<str:username>/', views.chat_with_user, name='chat_with_user'),
]