from django.urls import path

from .views import room, enter_room, register, authorization, logout_user

urlpatterns = [
    path('', enter_room, name='enter_room'),
    path('<str:room_name>/', room, name='chat-room'),
    path('reg', register, name='reg'),
    path('log', authorization, name='log'),
    path('logout', logout_user, name='logout'),
]
