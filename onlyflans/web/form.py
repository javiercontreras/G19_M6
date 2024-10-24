from django import forms

class MiFormulario(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Tu nombre'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Tu email'}))
    