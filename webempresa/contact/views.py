from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            print(email)
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage("La caffetiera: Nuevo mensaje de contacto",
                                 "De {}  {}\n\nEscribió:\n\n{}".format(
                                     name, email, content),
                                 "no-contestar@inbox.mailtrap.io",
                                 ["lajr1099@gmail.com"],
                                 reply_to=[email])
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien
                return redirect(reverse('contact')+"?fail")

    html_resposnse = render(
        request, "contact/contact.html", {"form": contact_form})

    return html_resposnse
