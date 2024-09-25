from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm, TorrentForm, ComentarioForm, UserLoginForm
from .models import Torrent, Comentario
from django.http import Http404, HttpResponse
import os

def inicio(request):
    torrents = Torrent.objects.order_by('-fecha_subida')[:10]  
    return render(request, 'home.html', {'torrents': torrents})

def usuarios(request):
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        login_form = UserLoginForm()

    return render(request, 'usuarios.html', {'login_form': login_form})

def crear_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'crear_usuario.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'usuarios.html', {'login_form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def cargar_torrent(request):
    if request.method == 'POST':
        form = TorrentForm(request.POST, request.FILES)
        if form.is_valid():
            torrent = form.save(commit=False)
            torrent.usuario = request.user 
            torrent.save() 
            return redirect('home')
    else:
        form = TorrentForm()
    return render(request, 'torrent.html', {'form': form})

def buscar_torrents(request):
    query = request.GET.get('q', '') 
    results = []
    if query:
        results = Torrent.objects.filter(nombre__icontains=query) | Torrent.objects.filter(descripcion__icontains=query)
    return render(request, 'search.html', {'results': results, 'query': query})


@login_required
def descargar_torrent(request, torrent_id):
    torrent = get_object_or_404(Torrent, id=torrent_id)
    file_path = torrent.archivo.path 

    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/x-bittorrent')
            response['Content-Disposition'] = f'attachment; filename="{torrent.nombre}.torrent"' 
            return response
    else:
        raise Http404("No se pudo encontrar el archivo")
    

@login_required
def eliminar_torrent(request, torrent_id):
    torrent = get_object_or_404(Torrent, id=torrent_id)
    if request.user == torrent.usuario:   
        torrent.delete()
    return redirect('home') 

@login_required
def comentario(request, torrent_id):
    torrent = get_object_or_404(Torrent, id=torrent_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.torrent = torrent
            comentario.save()
            return redirect('home')
    else:
        form = ComentarioForm()
    return render(request, 'dejar_comentario.html', {'form': form, 'torrent': torrent})

def detalles_torrent(request, torrent_id):
    torrent = get_object_or_404(Torrent, id=torrent_id)
    comentarios = Comentario.objects.filter(torrent=torrent)

    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.usuario = request.user
            comentario.torrent = torrent
            comentario.save()
            return redirect('detalles_torrent', torrent_id=torrent.id)
    else:
        comentario_form = ComentarioForm()

    return render(request, 'detalles.html', {
        'torrent': torrent,
        'comentarios': comentarios,
        'comentario_form': comentario_form
    })