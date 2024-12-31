from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from usuarios.forms import LoginForm, CadastroForm

# Create your views here.

def login(request):
    form = LoginForm()
    return render(request, "usuarios/login.html", {"form" : form})

def cadastro(request):
    print("Executando a função cadastro")
    form = CadastroForm()
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        print("Método é post")
        # check whether it's valid:
        form = CadastroForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required

            if form['senha_1'].value() != form['senha_2'].value() :
                return redirect('cadastro') 
            
            nome = form['nome_login'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()

            if User.objects.filter(username=nome).exists() :
                return redirect('cadastro')

            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            user.save()
            return redirect("login")

            
    return render(request, 'usuarios/cadastro.html', {"form" : form})