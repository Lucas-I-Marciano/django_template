from django.urls import path
from usuarios.views import login, cadastro, user_logout

urlpatterns = [
    path("login/", login, name="login"),
    path("cadastro/", cadastro, name="cadastro"),
    path("logout/", user_logout, name="logout")
]