from django.shortcuts import render, redirect
from django.contrib import messages

from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForm

# Create your views here.

def index(request):
    if not request.user.is_authenticated :
        messages.error(request, "Acesso restrito! Login necessário")
        return redirect('user_login')
    
    fotografias = Fotografia.objects.filter(publicado=True).order_by("-data_fotografia").all()
    return render(request, 'galeria/index.html', {"fotografias" : fotografias})

def imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def busca(request):
    if not request.user.is_authenticated :
        messages.error(request, "Acesso restrito! Login necessário")
        return redirect('user_login')
        
    fotografias = Fotografia.objects.filter(publicado=True).order_by("-data_fotografia").all()

    # To know more: https://docs.djangoproject.com/en/5.1/ref/request-response/
    if request.GET['buscar'] :
        texto_buscar = request.GET['buscar']
        fotografias = fotografias.filter(nome__icontains=texto_buscar)
    return render(request, "galeria/busca.html", {"fotografias" : fotografias})

def adicionar_imagem(request):
    form = FotografiaForm()
    return render(request, "galeria/adicionar_imagem.html", {"form" : form})