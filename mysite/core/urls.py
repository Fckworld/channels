# chat/urls.py
from django.urls import path

from . import views
app_name = 'core'
urlpatterns = [
    path("", views.index, name="index"),
    path("whatsapp/",views.mandar_whatsapp, name="whatsapp"),
]