import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ProductionConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add("production", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("production", self.channel_name)

    async def send_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))