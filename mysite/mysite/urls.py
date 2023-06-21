# mysite/urls.py
from django.contrib import admin
from django.urls import include, path
from chat import views

urlpatterns = [
    path("", include("core.urls")),
    path("chat/", include("chat.urls")),
    path("chatbot/", include("chatbot.urls")),
    path("webhook/", include("webhook.urls")),
    path("admin/", admin.site.urls),
]