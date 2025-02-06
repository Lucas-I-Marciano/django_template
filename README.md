# Universe Photo Gallery

## Project Overview
This is a full-stack project developed in Python using Django. The project is a photo gallery of the universe where users can post photos of planets, galaxies, nebulae, and stars.

Login
<img width="400" height="250" title="a title" alt="Alt text" src="https://github.com/user-attachments/assets/ae4a83a6-2fbf-4a1d-8791-d4f693f49e46">
Register
<img width="400" height="250" title="a title" alt="Alt text" src="https://github.com/user-attachments/assets/d30eea60-8cfe-4d31-98b6-985a3a126ad6">

Main
<img width="700" height="300" title="a title" alt="Alt text" src="https://github.com/user-attachments/assets/e56331c1-53fe-4ca1-b517-a7429a17f5a1">

## Project Structure
The project follows Django best practices and is organized as follows:
- **setup**: Contains project configuration files, including `settings.py`.
- **static**: Stores all static files.
- **media**: Stores images uploaded by users.
- **apps**: Contains the individual apps for the project, which are `galeria` and `usuarios`.

## Apps

### Galeria
The `galeria` app handles the photo gallery functionality. It includes the `Fotografia` model, which stores information about each photo, such as name, description, caption, storage location, and the user who posted it. The user field is a foreign key to the `usuarios` model.

#### Endpoints
- `path("", index, name="index")`: Displays all photos on the site.
- `path("imagem/<int:foto_id>", imagem, name="imagem")`: Displays a specific photo.
- `path("busca", busca, name="busca")`: Searches for photos based on a query.
- `path("adicionar-imagem", adicionar_imagem, name="adicionar_imagem")`: Adds a new photo.
- `path("editar-imagem/<int:foto_id>", editar_imagem, name="editar_imagem")`: Edits an existing photo.
- `path("excluir-imagem/<int:foto_id>", excluir_imagem, name="excluir_imagem")`: Deletes a photo.
- `path("filtrar-categoria/<str:categoria>", filtro_categoria, name="filtro_categoria")`: Filters photos by category (Planets, Galaxies, Nebulae, Stars).

### Usuarios
The `usuarios` app handles user registration and authentication. It includes forms for user login and registration using `django.forms.Form`. The views manage GET requests to display empty forms and POST requests to validate and process user data.

## Models

### Fotografia
```python
class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, null=False, default='')
    publicado = models.BooleanField(default=True)
    data_fotografia = models.DateField(default=datetime.now)
    usuario = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=False,
        null=True
    )
```

## How to Use
1. Clone the repository: `git clone https://github.com/Lucas-I-Marciano/django_template`
2. Navigate to the project directory: `cd django_template`
3. Create virtual env: `python -m venv venv`
4. Activate venv: `.\venv\Scripts\activate.ps1`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Apply migrations: `python manage.py migrate`
7. Create a superuser: `python manage.py createsuperuser`
8. Run the development server: `python manage.py runserver`
9. Access the application at `http://127.0.0.1:8000/`

## License
This project is licensed under the MIT License.

## Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Contact
For any questions or suggestions, please contact [Lucas I Marciano](https://github.com/Lucas-I-Marciano)
