from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from portfolio.form import ContactForm
from django.core.mail import send_mass_mail
from django.urls import reverse

# Create your views here.

def home(request):
    contact_form = ContactForm
    success_message = None
    if request.method == 'POST' and 'send_message' in request.POST:
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.save()
            
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']

            message1 = (subject, message, email, ['belovedtwinssurprises@gmail.com'])
            message2 = ('Beloved Twins', f'{email} Just sent: {message}', email, ['crypticwisdom84@gmail.com'])
            send_mass_mail((message1, message2), fail_silently=False)

            success_message = 'Your message has been sent'
    
    return render(request, 'portfolio/home.html', {
        'contact_form':contact_form,
        'success_message':success_message
    })