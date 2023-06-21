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

