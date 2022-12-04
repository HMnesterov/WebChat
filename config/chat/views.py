from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from chat.forms import RegisterForm


def enter_room(request):
    return render(request, 'enter_room.html')




def room(request, room_name):
    if not request.user.is_authenticated:
        return redirect('reg')
    return render(request, 'chatroom.html', {'room_name': room_name})




def register(request):
    form = RegisterForm()
    if request.method == 'POST':

        try:
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request=request, user=user)


        except:
            pass
    return render(request, 'register.html', {'form': form})
