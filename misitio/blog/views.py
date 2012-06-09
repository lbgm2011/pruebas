# Create your views here.
from blog.models import *
from django.shortcuts import render_to_response, get_object_or_404

def listado(request):
    publicaciones = Post.objects.all()
    return render_to_response('publicaciones.html', {'publicaciones':publicaciones})

def detalle(request, idpost):
    post = Post.objects.get(pk=idpost)
    galerias = post.galleries.all()
    return render_to_response('detalle.html', {'post':post, 'galerias':galerias})

def galerias(request):
    galerias = Galeria.objects.all()
    return render_to_response('galerias.html', {'galerias':galerias})

def detallegaleria(request, idgaleria):
    galeria = Galeria.objects.get(pk=idgaleria)
    fotos = Foto.objects.filter(galeria=galeria)
    return render_to_response('galeria.html', {'galeria':galeria, 'fotos':fotos})
