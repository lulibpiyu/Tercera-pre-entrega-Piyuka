from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Torrent(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='torrents/')  
    fecha_subida = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    contenido = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    torrent = models.ForeignKey(Torrent, on_delete=models.CASCADE) 
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.fecha_creacion.strftime('%Y-%m-%d %H:%M')}"
