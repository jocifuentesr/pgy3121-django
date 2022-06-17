from django.shortcuts import render


# Create your views here.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        super().__init__()


def home(request):
    lista = ["comer pantuflas", "pasear", "comer"]
    responsable = Persona("Humana Claudia", "35")
    contexto = {"nombre": "Kiara Pug", "actividades": lista, "responsable": responsable}
    return render(request, 'core/home.html', contexto)
