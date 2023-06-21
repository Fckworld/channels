from django.shortcuts import render, HttpResponse
import requests
# Create your views here.

def index(request):
    return render(request, "chatbot/index.html")

