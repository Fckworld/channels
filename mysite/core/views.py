import requests
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "core/home.html")

def mandar_whatsapp(request):
    url = 'https://graph.facebook.com/v17.0/107307359023784/messages'
    headers = {
        'Authorization': 'Bearer EABZAM6PEeUBMBADpGNYFbVNaTxPp9tLMi73x3ZBWllCi3iCOn0bh9h47F6xgZB8Np9QcqTlB6ZCrZC4HmMsZCkrAsn9tPpXbFauH6gxVqETBHae1tojms2r5m0ys8QxMAVmQBDvcLKZCRIvpjGTEQ1zgir1jYuOANsj5xElZAS7fu4hiGUlnEc6gZACqRDpg2ZCPgtOtNyTOT0T155dydhvTD786EPoTLBnX4ZD',
        'Content-Type': 'application/json'
    }
    data = {
        'messaging_product': 'whatsapp',
        'to': '56999318387',
        'type': 'template',
        'template': {
            'name': 'hello_world',
            'language': {
                'code': 'en_US'
            }
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.ok:
        return HttpResponse('Mensaje enviado correctamente')
    else:
        return HttpResponse('Error al enviar el mensaje', status=response.status_code)
