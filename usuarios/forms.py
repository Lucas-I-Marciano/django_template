from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder": "Ex.: João Silva",
            }
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder": "Digite sua senha",
            }
        )
    )

class CadastroForm(forms.Form):
    nome_login = forms.CharField(
        label="Nome Completo",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder": "Ex.: João Silva",
            }
        )
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class" : "form-control",
                "placeholder": "Ex.: jsilva@xpto.com",
            }
        )
    )

    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder": "Digite sua senha",
            }
        )
    )

    senha_2 = forms.CharField(
        label="Confirme a Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder": "Digite novamente a senha",
            }
        )
    )

    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 != senha_2:
            raise ValidationError("As senhas são diferentes")

        return senha_2

        
    def clean_nome_login(self):
        nome_login = self.cleaned_data.get("nome_login")

        if nome_login:
            nome_login = nome_login.strip()

            if ' ' in nome_login :
                raise ValidationError("Espaços não são permitidos nesse campo")
            
            if User.objects.filter(username=nome_login).exists() :
                raise ValidationError("Usuário já cadastrado")


        return nome_login
        
    