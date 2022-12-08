from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from chat import urls
from chat.views import enter_room

urlpatterns = [
    path('', enter_room, name='enter_room'),
    path('admin/', admin.site.urls),
    path('chat/', include(urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
