from django import forms
from apps.galeria.models import Fotografia

class FotografiaForm(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicado']

        widgets = {
            "nome" : forms.TextInput(attrs={"class":"form-control"}) ,
            "legenda" : forms.TextInput(attrs={"class":"form-control"}),
            "descricao" : forms.Textarea(attrs={"class":"form-control"}),
            "foto" : forms.FileInput(attrs={"class":"form-control"}),
            "categoria" : forms.Select(attrs={"class":"form-control"}),
            "data_fotografia" : forms.DateInput(
                format = "%Y/%m/%d",
                attrs={
                    "class":"form-control",
                    "placeholder": "YYYY/MM/DD",
                    "type":"date"
                    }
                ),
            "usuario" : forms.Select(attrs={"class":"form-control"})
        }