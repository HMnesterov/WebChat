from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
"""URLS FOR ASGI UPDATE(ASYNC)"""
application = {
    ProtocolTypeRouter({
        "websocket": AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns
            ),
        ),
    })
}
