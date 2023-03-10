from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Inicio (request):
    return render(request, 'inicio.html')


def About (request):
    return render(request,"about.html")


def contact(request):
    return render(request,"contact.html")

