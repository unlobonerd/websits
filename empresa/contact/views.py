from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForms
from django.core.mail import EmailMessage



# Create your views here.
def contact(request):
    contact_form = ContactForms()

    if request.method == "POST":
        contact_form = ContactForms(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #revio
            
            email = EmailMessage(
                "LA Caffetiera: Nuevo Mensaje",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "contesstar@mailtrap.io",
                ["luismiguel@gmail.com"],
                reply_to=[email]
                )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                
                return redirect(reverse('contact')+"?fail")


    return  render(request, "contact/contact.html", {'form':contact_form})