import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import re_path  # Usar re_path para captura de parâmetros
from chat import consumers  # Importação do consumidor

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ICampi.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(  # WebSocket precisa estar no middleware correto
        URLRouter([
            re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),  # Certifique-se de que a URL está correta
        ])
    ),
})