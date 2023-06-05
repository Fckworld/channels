import os
import django
from django.conf import settings
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Configura la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Carga las configuraciones de Django
django.setup()

# Accede a la configuración CHANNEL_LAYERS
channel_layers = settings.CHANNEL_LAYERS

# Obtén una instancia del channel_layer
channel_layer = get_channel_layer()

# Obtén los mensajes utilizando InMemoryChannelLayer
messages = async_to_sync(channel_layer.receive_many)(["specific..inmemory!GLwKWccdiWUY"])

# Imprimir los contenidos de los mensajes
for message in messages:
    content = message.get('content', None)
    print(content)