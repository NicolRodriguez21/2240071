# Paddock — Directorio de pilotos F1 y F2

Proyecto académico CRUD construido con Django y SQLite, a partir del proyecto base del curso.

## Requisitos
- Python 3.10 o superior
- pip

## Instalación en Windows
1. Descomprime el ZIP y abre una terminal en la carpeta que contiene `manage.py`.
2. Crea y activa un entorno virtual (opcional pero recomendado):
   ```powershell
   py -m venv venv
   .\venv\Scripts\activate
   ```
3. Instala Django:
   ```powershell
   pip install -r requirements.txt
   ```
4. Aplica migraciones:
   ```powershell
   python manage.py migrate
   ```
5. Crea un usuario para entrar al sitio:
   ```powershell
   python manage.py createsuperuser
   ```
   Si tu base de datos original conserva el usuario `admin`, puedes intentar iniciar con `admin/admin`; si no funciona, crea un superusuario nuevo.
6. Inicia el servidor:
   ```powershell
   python manage.py runserver
   ```
7. Abre http://127.0.0.1:8000/ . Inicia sesión para crear y gestionar tus propios pilotos. El panel administrativo está en http://127.0.0.1:8000/admin/ .

## Funcionalidades
- Modelo `Piloto` relacionado con el usuario autenticado.
- CRUD completo: listado, detalle, creación, edición y eliminación con confirmación.
- Búsqueda por nombre, nacionalidad o escudería; filtros por categoría y escudería.
- Paginación de seis registros por página conservando los filtros.
- Validación de edad (16–70) y año de debut (1950–2100), en formulario y base de datos.
- Fotografías servidas desde `modulo/static/modulo/img/`, aprovechando las imágenes incluidas en el proyecto base.
- Panel de administración de Django.

## Fotografías
En el campo **Archivo de imagen** escribe el nombre exacto de una imagen dentro de `modulo/static/modulo/img/`, por ejemplo `max-verstappen-2026.png`. Si se deja vacío, se muestra una inicial de reemplazo.

## Modelo y decisiones
Cada piloto tiene nombre, categoría, escudería, edad, año de debut, nacionalidad, descripción, archivo de imagen y usuario responsable. La relación con `User` permite asociar cada perfil a su creador y mostrar a cada usuario solo sus propios registros en la interfaz. Se valida que la edad esté entre 16 y 70 años y que el año de debut esté entre 1950 y 2100.
