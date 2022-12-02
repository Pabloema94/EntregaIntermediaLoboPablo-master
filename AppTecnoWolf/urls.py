from django.urls import path
from AppFightwear.views import *

urlpatterns = [
    
    path("inicio", inicio, name="inicio"),
    path("disco", disco, name="disco"),
    path("impresora3D", impresora3D, name="Impresora3D"),
    path("compu", compu, name="compu"),
    path("busqueda_disco", busqueda_disco, name="busqueda_disco"),
    path("resultado_busqueda", resultado_busqueda_disco, name="resultado_busqueda_disco"),


]
