from django.shortcuts import render
from django.http import HttpResponse
from galeria.models import Fotografia

# Create your views here.

def index(request):
    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {"fotografias" : fotografias})

def imagem(request):
    return render(request, 'galeria/imagem.html')