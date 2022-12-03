from django.shortcuts import render
from AppTecnoWolf.forms import *
from AppTecnoWolf.models import *

def inicio(request):
    return render(request, "inicio.html",{"mensaje_inicio":"Técnologia Shop"})


def impresora3D(request):
    if request.method == "POST":
        info_form_impresora3D = FormImpresora3D(request.POST)
        if info_form_impresora3D.is_valid():
            form_limpio = info_form_impresora3D.cleaned_data
            Impresora3D_ingresada= Impresora3D(marca = form_limpio["marca"], modelo = form_limpio["modelo"], tipo = form_limpio["tipo"], precio = form_limpio["precio"])
            Impresora3D_ingresada.save()
            return render(request, "inicio.html", {"mensaje_inicio":"Impresora 3D ingresada exitosamente"})
        else:
            form_vacio_Impresora3D = FormImpresora3D()
            return render(request, "Impresora3D.html", {"codigo" : form_vacio_Impresora3D})
    
    return render(request, "Impresora3D.html")


def compu(request):
    if request.method == "POST":
        info_form_compu = FormCompu(request.POST)
        if info_form_compu.is_valid():
            form_limpio = info_form_compu.cleaned_data
            compu_ingresada = Compu(marca = form_limpio["marca"], modelo = form_limpio["modelo"], tipo = form_limpio["tipo"],  precio = form_limpio["precio"])
            compu_ingresada.save()
            return render(request, "inicio.html", {"mensaje_inicio":"Compu ingresadas exitosamente"})
    else:
        form_vacio_compu = FormCompu()
        return render(request, "compu.html", {"codigo" : form_vacio_compu})

    return render(request, "compu.html")


def disco(request):
    if request.method == "POST":
        info_form_disco = FormDisco(request.POST)
        if info_form_disco.is_valid():
            form_limpio = info_form_disco.cleaned_data
            disco_ingresado = Disco(marca = form_limpio["marca"], modelo = form_limpio["modelo"], tipo = form_limpio["tipo"], precio = form_limpio["precio"])
            disco_ingresado.save()
            return render(request, "inicio.html", {"mensaje_inicio":"Disco ingresado con éxito!"})
    else:
        form_vacio_disco = FormDisco()
        return render(request, "disco.html", {"codigo" : form_vacio_disco})

    return render(request, "disco.html")


def busqueda_disco(request):
    
    return render (request, "busqueda_disco.html")



def resultado_busqueda_disco(request):
    valor_url = request.GET["marca"]
    if valor_url != "":
        disco_filtrados = Disco.objects.filter(marca = valor_url)  
        print(disco_filtrados)
        print('-------------------------------------------------------------------------------------------------------------')
        return render(request, "resultado_busqueda_disco.html", {'disco_seleccionados': disco_filtrados })
    else:
        return render(request, "busqueda_disco.html")