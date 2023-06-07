# mysite/urls.py
from django.contrib import admin
from django.urls import include, path
from chat import views

urlpatterns = [
    path("chat/", include("chat.urls")),
    path("chatbot/", include("chatbot.urls")),
    path("admin/", admin.site.urls),
    path('ver-mensajes/', views.ver_mensajes, name='ver_mensajes'),
]