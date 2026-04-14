from django.shortcuts import render
from .models import Organizacion

def index(request):
    organizaciones = Organizacion.objects.all()
    return render(request, 'socios/index.html', {'organizaciones': organizaciones})

def detalle(request, id):
    organizacion = Organizacion.objects.get(id=id)
    return render(request, 'socios/detalle.html', {'organizacion': organizacion})
