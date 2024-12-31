from django.shortcuts import render

from usuarios.forms import LoginForm, CadastroForm

# Create your views here.

def login(request):
    form = LoginForm()
    return render(request, "usuarios/login.html", {"form" : form})

def cadastro(request):
    form = CadastroForm()
    return render(request, 'usuarios/cadastro.html', {"form" : form})