from django import forms
from django.contrib.auth.models import User
from .models import Usuario, Torrent, Comentario
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class BuscarTorrentForm(forms.Form):
    query = forms.CharField(max_length=200)

class UsuarioForm(forms.ModelForm):
    class Meta: 
        model = Usuario
        fields = ['nombre', 'email']

class TorrentForm(forms.ModelForm):
    class Meta:
        model = Torrent
        fields = ['nombre', 'descripcion', 'archivo']
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']