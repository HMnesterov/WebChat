from django.contrib import admin
from django.urls import path, include
from chat import urls
from  chat.views import enter_room
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include(urls)),
    path('', enter_room, name='enter_room')
]
