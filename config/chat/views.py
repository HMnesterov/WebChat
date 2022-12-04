from django.shortcuts import render

def enter_room(request):
    return render(request, 'enter_room.html')

def room(request, room_name):
    return render(request, 'chatroom.html', {'room_name': room_name})
