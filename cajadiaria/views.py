from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CuentaForm
from cajadiaria.models import Cuenta,TipoCuenta,CajaDiaria
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

def post_list(request):
    cuenta=Cuenta.objects.all()
    return render(request,'cajadiaria/post_list.html',{'cuenta':cuenta})

def detallecaja(request,pk):
    post=get_object_or_404(Cuenta,pk=pk)
    return render(request,'cajadiaria/detallecaja.html',{'post':post})

@login_required
def cuenta_nueva(request):
    if request.method=="POST":
        formulario=CuentaForm(request.POST)
        if formulario.is_valid():
            cuenta=Cuenta.objects.create(nombre=formulario.cleaned_data['nombre'],fecha=formulario.cleaned_data['fecha'],descripcion=formulario.cleaned_data['descripcion'],monto=formulario.cleaned_data['monto'])
            for tipocuenta_id in request.POST.getlist('cajas'):
                cajadiaria=CajaDiaria(tipocuenta_id=tipocuenta_id,cuenta_id=cuenta.id)
                cajadiaria.save()
                return redirect('detallecaja',pk=cajadiaria.pk)

    else:
        formulario=CuentaForm();
    return render(request,'cajadiaria/cuenta_editar.html',{'formulario':formulario})
