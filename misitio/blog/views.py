# Create your views here.
from blog.models import Post, Author
from django.shortcuts import render_to_response, get_object_or_404

def listado(request):
    publicaciones = Post.objects.all()
    return render_to_response('publicaciones.html', {'publicaciones':publicaciones})

def detalle(request, idpost):
    post = Post.objects.get(pk=idpost)
    return render_to_response('detalle.html', {'post':post})
