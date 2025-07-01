from django.shortcuts import render
from .dados import habilidades


def home(request):
    return render(request, 'home.html', {'habilidades': habilidades})