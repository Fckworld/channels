# chat/consumers.py
import json

from channels.generic.websocket import WebsocketConsumer

from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):

        self.room_group_name = 'test'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print("SE HA CONECTADO")
        print(f"Canal agregado al grupo. Nombre del canal: {self.channel_name}")

        self.accept()

    def disconnect(self, close_code):
        print("SE HA DESCONECTADO")
        pass

    def receive(self, text_data):
       
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        #self.send(text_data=json.dumps({"message": message}))
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message': message
            }
        )
        print("SE HA RECIBIDO")
    
    def chat_message(self,event):
        message = event['message']
        self.send(text_data = json.dumps(
            {
                'type':'chat',
                'message':message
            }
        ))

        print('Se ha llamado : CHAT_MESSAGE')