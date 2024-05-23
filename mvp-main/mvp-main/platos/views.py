from django.shortcuts import render
from django.conf import settings

def index(request):
    
    restaurantes = settings.DB["TDC"]

    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        edad = request.POST.get("edad")
        nacionalidad = request.POST.get("nacionalidad")
        num_tarjeta = request.POST.get("num_tarjeta")

        if nombre and edad and nacionalidad:
            nueva_asignacion = {
                "nombre": nombre,
                "edad": edad,
                "nacionalidad": nacionalidad,
                "num_tarjeta": num_tarjeta
            }
            restaurantes.insert_one(nueva_asignacion)

    total_asignaciones = restaurantes.count_documents({})
    asignaciones = list(restaurantes.find())

    return render(request, "lista_platos.html", {
        'asignaciones': asignaciones,
        'total_asignaciones': total_asignaciones
    })

def solicitudes(request):

    asignaciones = settings.DB["TDC"]
    total = asignaciones.find()
    total_asignaciones = asignaciones.count_documents({})

    return render(request, "asignaciones.html", {'asignaciones': total, 'total_asignaciones': total_asignaciones})
