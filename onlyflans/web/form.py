from django import forms
from .models import Flan, ContactForm

class MiFormulario(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Tu nombre'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Tu email'}))
    

class ContactForm(forms.ModelForm):
    class Meta:
        model= ContactForm
        fields = ['contact_form_uuid','customer_name','customer_email','message']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),  
            'customer_email': forms.EmailInput(attrs={'class': 'form-control', 'min': 0}),
            'message': forms.Textarea(attrs={'rows': 3, 'cols': 40,'class':'form-control'}),
        }