from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages

# Create your views here.

def mainPage(request):
    group = Pages.objects.all()
    list = ''
    for item in group:
        list = list + item.name + '<br>'
    return HttpResponse("La lista de recursos disponibles es la siguiente:<br><br>" +
    list + '<br>'
    "Un ejemplo de cómo pedir un recurso es: "
    "http://localhost:8000/pepito<br><br>"
    "Si pides un recurso que no existe, la página te lo indicará")

def getPage(request, text):
    try:
        object = Pages.objects.get(name = text)
        return HttpResponse(object.page)
    except Pages.DoesNotExist:
        return HttpResponse("No hay una página para " + text)
