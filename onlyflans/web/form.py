from django import forms
from .models import Flan, ContactForm

class MiFormulario(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Tu nombre'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Tu email'}))
    

class ContactForm(forms.Form):
    class Meta:
        form = ContactForm
        fields = ['contact_form_uuid','customer_name','customer_email',]