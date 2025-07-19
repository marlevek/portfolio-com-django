from django.shortcuts import render
from .models import Habilidade, Projeto


def home(request):
    habilidades = Habilidade.objects.all()
    return render(request, 'home.html', {'habilidades': habilidades})


def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos.html', {'projetos': projetos})


def detalhes_projeto(request, id_projeto):
    projeto = Projeto.objects.get(id=id_projeto)
    return render(request, 'detalhes_projeto.html', {'projeto': projeto})
