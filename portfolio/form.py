from django import forms
from django.forms import fields
from portfolio.models import Contact

class ContactForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter Your Name ...',
        'class':'form-control'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Enter Email ...',
        'class':'form-control',
    }))

    subject = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter A Subject ...',
        'class':'form-control',
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'Enter A Message ...',
        'class':'form-control'
    }))


    class Meta:

        model = Contact
        fields = '__all__'