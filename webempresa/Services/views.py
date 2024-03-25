from django.shortcuts import render
from .models import Service

# Create your views here.


def services(request):
    services = Service.objects.all()
    html_resposnse = render(
        request, "services/services.html", {'services': services})

    return html_resposnse
