# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("request-wha-meta-api",views.enviar_mensaje_whatsapp,name="api.request.whatsapp")
]