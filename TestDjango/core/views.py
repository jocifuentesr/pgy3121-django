from django.shortcuts import render
from .models import Vehiculo

# Create your views here.


def home(request):
    vehiculos = Vehiculo.objects.all()
    datos = {
        'vehiculos': vehiculos
    }
    return render(request, 'core/home.html', datos)
