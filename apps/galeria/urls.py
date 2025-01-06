from django.urls import path

from apps.galeria.views import index, imagem, busca, adicionar_imagem, editar_imagem, excluir_imagem, filtro_categoria

urlpatterns = [
    path("", index, name="index"),
    path("imagem/<int:foto_id>", imagem, name="imagem"),
    path("busca", busca, name="busca"),
    path("adicionar-imagem", adicionar_imagem, name="adicionar_imagem"),
    path("editar-imagem/<int:foto_id>", editar_imagem, name="editar_imagem"),
    path("excluir-imagem/<int:foto_id>", excluir_imagem, name="excluir_imagem"),
    path("filtrar-categoria/<str:categoria>", filtro_categoria, name="filtro_categoria"),
]