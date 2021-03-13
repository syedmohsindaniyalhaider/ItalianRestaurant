from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def index(request):
    return render(request, 'restapp/index.html')

def about(request):
    return render(request, 'restapp/about.html')

def contact(request):
    return render(request, 'restapp/contact.html')

def menu(request):
    return render(request, 'restapp/menu.html')