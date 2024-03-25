from django.shortcuts import render

# Create your views here.


def home(request):
    html_resposnse = render(request, "core/home.html")
    return html_resposnse


def about(request):
    html_resposnse = render(request, "core/about.html")

    return html_resposnse


def store(request):
    html_resposnse = render(request, "core/store.html")

    return html_resposnse
