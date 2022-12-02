from django import forms

class FormDisco(forms.Form):
    marca=forms.CharField(max_length=50)
    modelo=forms.CharField(max_length=20)
    tipo=forms.CharField(max_length=20)
    precio=forms.IntegerField()

class FormCompu(forms.Form):
    marca= forms.CharField(max_length=50)
    modelo= forms.CharField(max_length=50)
    tipo= forms.CharField(max_length=20)
    precio= forms.IntegerField()

class FormImpresora3D(forms.Form):
    marca= forms.CharField(max_length=50)
    modelo= forms.CharField(max_length=50)
    tipo= forms.CharField(max_length=20)
    precio= forms.IntegerField()