from django import forms
from personajes.models import vaquero

class Formvaquero(forms.ModelForm):
    class Meta:
        model = vaquero
        fields = '__all__'