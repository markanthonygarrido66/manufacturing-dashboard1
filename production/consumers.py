import json
from channels.generic.websocket import AsyncWebsocketConsumer

class LiveConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add("live_system", self.channel_name)
        await self.accept()
        print("WS CONNECTED")
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("live_system", self.channel_name)

    async def send_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))