from django.contrib import admin
from chatbot.models import *
# Register your models here.
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('id','message')
#admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(ChatMessage,ChatMessageAdmin)