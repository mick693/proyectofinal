from django.db import models
from django.contrib import admin

class TipoCuenta(models.Model):
    tipo=models.CharField(max_length=30)

    def __str__(self):
        return self.tipo
#77636966
class Cuenta(models.Model):
    nombre=models.CharField(max_length=40)
    fecha=models.DateField()
    descripcion=models.TextField()
    monto=models.IntegerField()
    cajas=models.ManyToManyField(TipoCuenta,through='CajaDiaria')
    def __str__(self):
        return self.nombre

class CajaDiaria(models.Model):
    tipocuenta=models.ForeignKey(TipoCuenta,on_delete=models.CASCADE)
    cuenta=models.ForeignKey(Cuenta,on_delete=models.CASCADE)

class CajaDiariaInLine(admin.TabularInline):
    model=CajaDiaria
    extra=1

class TipoCuentaAdmin(admin.ModelAdmin):
    inlines=(CajaDiariaInLine,)

class CuentaAdmin(admin.ModelAdmin):
    inlines=(CajaDiariaInLine,)
# Create your models here.
