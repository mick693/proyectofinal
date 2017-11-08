from django.shortcuts import render
from django.contrib import messages
from .forms import CuentaForm
from cajadiaria.models import Cuenta,TipoCuenta,CajaDiaria

def post_list(request):
    return render(request,'cajadiaria/post_list.html')

def cuenta_nueva(request):
    if request.method=="POST":
        formulario=CuentaForm(request.POST)
        if formulario.is_valid():
            cuenta=Cuenta.objects.create(nombre=formulario.cleaned_data['nombre'],fecha=formulario.cleaned_data['fecha'],descripcion=formulario.cleaned_data['descripcion'],monto=formulario.cleaned_data['monto'])
            for cuenta_id in request.POST.getlist('cajas'):
                cajadiaria=CajaDiaria(cuenta_id=actor_id,pelicula_id=pelicula_id)
                cajadiaria.save()
            messages.add_messages(request,messages.SUCCESS,'Cuenta agregada exitosamente')
    else:
        formulario=CuentaForm();
    return render(request,'cajadiaria/cuenta_editar.html',{'formulario':formulario})
