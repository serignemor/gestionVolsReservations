from django import forms
from .models import Compagnie


class CompagnieForm(forms.ModelForm):
    nom = forms.CharField(max_length=25)
    logo = forms.ImageField(required=True)

    class Meta:
        model = Compagnie
        fields = ('nom', 'logo')
