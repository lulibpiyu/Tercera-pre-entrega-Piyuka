## Instalación

1. Clona este repositorio.
2. Crea y activa un entorno virtual (opcional, pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux o Mac
   venv\Scripts\activate  # Para Windows


Instalar las dependencias:
pip install -r requirements.txt

Realizar las migraciones:
python manage.py migrate

Iniciar el servidor:
python manage.py runserver

Funcionalidades
- Registro e inicio de sesión de usuarios.
- Subida y descarga de torrents (solo para usuarios logueados).
- Búsqueda de torrents (disponible para todos los usuarios).
- Comentarios sobre los torrents (solo para usuarios logueados).
- Eliminación de torrents (solo por el usuario que los subió).
- Listado de los últimos 20 torrents subidos.
- Sistema de permisos: solo el usuario que subió el torrent puede eliminarlo.



Torrent: Representa un archivo torrent subido por los usuarios.
nombre: Nombre del archivo.
archivo: Archivo .torrent.
usuario: Usuario que subió el archivo.
fecha_subida: Fecha en que el archivo fue subido.

Comentario: Representa los comentarios dejados por los usuarios en los torrents.
contenido: Texto del comentario.
usuario: Usuario que dejó el comentario.
torrent: El torrent sobre el cual se dejó el comentario.