from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def chat_view(request, room_name):
    return render(request, 'chat/chat.html', {
        'room_name': room_name
    })
    
def chat_with_user(request, username):
    other_user = get_object_or_404(User, username=username)
    return render(request, 'chat/chat.html', {'room_name': username, 'other_user': other_user})
