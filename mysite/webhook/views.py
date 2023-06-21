from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        # Obtener el cuerpo del mensaje
        data = json.loads(request.body)
        
        # Procesar el mensaje según tus necesidades
        # ...
        
        # Enviar una solicitud a Meta API con el token de autenticación
        url = 'https://api.metaapi.cloud/v1/some-endpoint'  # URL de Meta API
        meta_api_token = 'tu_token_de_autenticacion_aqui'  # Tu token de autenticación
        
        headers = {'Authorization': 'Bearer ' + meta_api_token}
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            # Procesar la respuesta exitosa de Meta API
            # ...
            return HttpResponse(status=200)
        else:
            # Procesar la respuesta con error de Meta API
            # ...
            return HttpResponse(status=500)  # O el código de estado apropiado en caso de error
    else:
        return HttpResponse(status=405)  # Método no permitido