from django.contrib import admin
from django.urls import path, include
from chat import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include(urls))
]
