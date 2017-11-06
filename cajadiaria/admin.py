from django.contrib import admin
from cajadiaria.models import Cuenta, CuentaAdmin, TipoCuenta, TipoCuentaAdmin

admin.site.register(Cuenta,CuentaAdmin)
admin.site.register(TipoCuenta,TipoCuentaAdmin)


# Register your models here.
