# chat/views.py
from django.shortcuts import render
from django.http import HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.conf import settings


def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

def ver_mensajes(request):
    channel_layer = get_channel_layer()

    # Nombre del canal específico del que deseas obtener los mensajes
    channel_name = "specific..inmemory!GLwKWccdiWUY"

    # Obtener los mensajes utilizando InMemoryChannelLayer
    messages = channel_layer._channel_layers[channel_name]

    # Construir una respuesta con los contenidos de los mensajes
    response_content = ""
    for message in messages:
        content = message.get('content', None)
        response_content += content + "\n"

    return HttpResponse(response_content)