from django import forms
from .models import Contacto

class DataForm(forms.ModelForm):
    class Meta:
        model=Contacto
        fields='__all__'


#Formulario de hoja de vida
#class ResumeCreate(forms.ModelForm):
#    model = Contacto
#    success_url = reverse_lazy('')
#    fields='__all__'
