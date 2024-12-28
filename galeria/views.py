from django.shortcuts import render
from django.http import HttpResponse
from galeria.models import Fotografia

# Create your views here.

def index(request):
    fotografias = Fotografia.objects.filter(publicado=True).order_by("-data_fotografia").all()
    return render(request, 'galeria/index.html', {"fotografias" : fotografias})

def imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def busca(request):
    return render(request, "galeria/busca.html")