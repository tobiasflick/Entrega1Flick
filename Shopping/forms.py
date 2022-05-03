from django import forms

class Formulario(forms.Form):
    nombre=forms.CharField()
    edad=forms.IntegerField()
    email=forms.EmailField()