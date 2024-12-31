from django import forms


class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login"
    )
    senha = forms.CharField(
        label="Senha"
    )
    