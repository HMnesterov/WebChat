from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from chat.forms import RegisterForm, LoginForm


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
                return redirect('enter_room')
        except:
            pass
    return render(request, 'register.html', {'form': form})



def authorization(request):
    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request=request, user=user)

            return redirect('enter_room')

    return render(request, 'register.html', {'form': form})



@login_required(login_url=reverse_lazy('log'))
def logout_user(request):
    logout(request)
    return redirect('log')