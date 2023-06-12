from django.shortcuts import render, HttpResponse
import requests
# Create your views here.

def index(request):
    return render(request, "chatbot/index.html")


def enviar_mensaje_whatsapp(request):

    url = 'https://graph.facebook.com/v17.0/107307359023784/messages'
    headers = {
        'Authorization': 'Bearer EABZAM6PEeUBMBANlLWHivzqQPcZBLnyl3xPsZC1paugh4Psh9jXagBqclZCZAgm3YD8IqOtTedWlwFNbvLjItlFBotWqUuU3xZBZCKZATtkMUQdqjZAZA05OVipiHjj4sbLTJUvM3nKGmxZAqWzNjxmyP48lkIaFrnEyKlZCLkdA9bNsvro6MVuYPl0jpfY3uTgFs6HZCEa72mSFd3bM8ZAfD9ZCqM3Ote0kwYg5wYZD',
        'Content-Type': 'application/json'
    }
    # data = {
    #     'messaging_product': 'whatsapp',
    #     'to': '56999318387',
    #     'type': 'template',
    #     'template': {
    #         'name': 'hello_world',
    #         'language': {'code': 'en_US'}
    #     }
    # }
    data = {
        'messaging_product': 'whatsapp',
        'to': '56999318387',
        'type': 'text',
        'text': {
            'preview_url': False,
            'body': 'que paaazaaaaa'
        }
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.ok:
        return HttpResponse("Mensaje enviado exitosamente.")
    else:
        return HttpResponse("Error al enviar el mensaje.")