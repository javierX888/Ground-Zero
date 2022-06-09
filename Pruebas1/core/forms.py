from django import forms
from django.forms import ModelForm
from .models import Pinturas

class PinturasForm(ModelForm):
    class Meta:
        model = Pinturas
        fields = ['idPintura','nombre_pintura','precio_pintura','autor','categoria']