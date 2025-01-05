from django.forms import ModelForm
from apps.galeria.models import Fotografia

class FotografiaForm(ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicado']