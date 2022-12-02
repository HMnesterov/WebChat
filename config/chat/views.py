from django.shortcuts import render

def enter_room(request):
    return render(request, 'enter_room.html')
def room(request, room_name):
    return render(request, 'room_page.html', {'room': room_name})
