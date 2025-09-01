from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from .models import ChatRoom, ChatMessage


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        if not self.scope["user"].is_authenticated:
            await self.close()
            return

        self.room_slug = self.scope['url_route']['kwargs']['slug']
        self.room_group_name = 'chat_%s' % self.room_slug

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data): 
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room_slug = data['room']

        saved_message = await self.save_message(username, room_slug, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': saved_message.message_content,
                'username': saved_message.user.username,
                'room': saved_message.room.slug,
                'timestamp': saved_message.date.strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room = event['room']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room': room,
        }))

    @sync_to_async
    def save_message(self,username,room,message):
        user = User.objects.get(username=username)
        room = ChatRoom.objects.get(slug=room)
        return ChatMessage.objects.create(user=user,room=room,message_content=message)


