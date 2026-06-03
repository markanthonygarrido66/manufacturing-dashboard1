from django.urls import path
from .consumers import ProductionConsumer

websocket_urlpatterns = [
    path("ws/production/", ProductionConsumer.as_asgi()),
]