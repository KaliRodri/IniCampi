import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Recebe o nome da sala a partir da URL
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Cria o grupo para onde as mensagens serão enviadas
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Sai do grupo ao desconectar
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Recebe uma mensagem de WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Envia a mensagem para o grupo de chat
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Recebe a mensagem do grupo de chat
    async def chat_message(self, event):
        message = event['message']

        # Envia a mensagem para o WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
        
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Recebe o nome da sala a partir da URL
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print(f"Connecting to room: {self.room_name}")  # Verifique o nome da sala
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()