from django import forms
from .models import *


class ActiuneForm(forms.ModelForm):
    class Meta:
        model = Actiune#genulFilmului
        fields = ('Nume','Filmul','Nota')#Fieldurile ce trebuie sa fie adaugate

class HorrorForm(forms.ModelForm):
    class Meta:
        model = Horror
        fields = ('Nume','Filmul','Nota')


class ComedieForm(forms.ModelForm):
    class Meta:
        model = Comedie
        fields = ('Nume','Filmul','Nota')


class DramaForm(forms.ModelForm):
    class Meta:
        model = Drama
        fields = ('Nume','Filmul','Nota')

