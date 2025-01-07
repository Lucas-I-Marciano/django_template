from django.urls import path
from apps.usuarios.views import user_login, cadastro, user_logout

urlpatterns = [
    path("login/", user_login, name="user_login"),
    path("cadastro/", cadastro, name="cadastro"),
    path("logout/", user_logout, name="logout")
]