import requests
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, "core/home.html")

@csrf_exempt
def mandar_whatsapp(request):
    print('LLAMANDO A MANDAR WAHTSAPP')
    for key, value in request.POST.items():
            # Realiza las operaciones necesarias con cada campo y su valor
            print(f'Campo: {key}, Valor: {value}')
    if request.method == 'POST':

        mensaje = request.POST.get('mensaje_whatsapp_envio')

        print(mensaje)

        url = 'https://graph.facebook.com/v17.0/107307359023784/messages'
        headers = {
            'Authorization': 'Bearer EABZAM6PEeUBMBADpGNYFbVNaTxPp9tLMi73x3ZBWllCi3iCOn0bh9h47F6xgZB8Np9QcqTlB6ZCrZC4HmMsZCkrAsn9tPpXbFauH6gxVqETBHae1tojms2r5m0ys8QxMAVmQBDvcLKZCRIvpjGTEQ1zgir1jYuOANsj5xElZAS7fu4hiGUlnEc6gZACqRDpg2ZCPgtOtNyTOT0T155dydhvTD786EPoTLBnX4ZD',
            'Content-Type': 'application/json'
        }
        data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": "56999318387",
        "type": "text",
        "text": { 
                "preview_url": False,
                "body":mensaje,
            }
        }

        response = requests.post(url, headers=headers, json=data)

        if response.ok:
            return HttpResponse('Mensaje enviado correctamente')
        else:
            return HttpResponse('Error al enviar el mensaje', status=response.status_code)
        print('PASAMOS EL IF')

    else:
        return HttpResponse('NO FUE UN METODO POST')
