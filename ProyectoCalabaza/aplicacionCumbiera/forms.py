from django import forms

# mismos datos q tiene cada clase en modelo.
class CursoForm(forms.Form):
    curso = forms.CharField(max_length=50)
    comision = forms.IntegerField()

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=50)

class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()

class EntregableForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    fecha_entrega= forms.DateField()
    entregado= forms.BooleanField()
