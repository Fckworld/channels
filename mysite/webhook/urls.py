from . import views
from django.urls import path

urlpatterns = [
    path('', views.webhook, name='webhook'),
    path('webhook/', views.webhook, name='webhook')
]