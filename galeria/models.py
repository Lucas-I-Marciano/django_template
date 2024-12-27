from django.db import models

# Create your models here.

class Fotografia(models.Model):
    CATEGORIAS = [
        #  1st element -> stored in the database. 2nd element -> displayed.
        ("nebulosa", "Nebulosa"),
        ("estrela", "Estrela"),
        ("galaxia", "Galáxia"),
        ("planeta", "Planeta")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, null=False, default='')

    def __str__(self):
        return f'Fotografia: [Nome: {self.nome}]'