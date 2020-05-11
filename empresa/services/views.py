from django.shortcuts import render
from .models import Services  #importamos el modelo osea la tabla donde estan el contenido

# Create your views here.
def services(request):
    services = Services.objects.all() #llamas a toda la tabla esto es ifuala selct * from services
    return  render(request, "services/services.html", {'services':services})