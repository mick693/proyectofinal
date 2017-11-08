from django import forms
from .models import Cuenta, TipoCuenta


class CuentaForm(forms.ModelForm):

    class Meta:
        model = Cuenta
        fields = ('nombre', 'fecha', 'descripcion','monto','cajas')
def __init__ (self, *args, **kwargs):
        super(CuentaForm, self).__init__(*args, **kwargs)
        self.fields["cajas"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["cajas"].help_text = "Seleccione ubicación de cuenta"
        self.fields["cajas"].queryset = TipoCuenta.objects.all()
