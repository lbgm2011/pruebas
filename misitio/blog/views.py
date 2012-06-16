# Create your views here.
from blog.models import *
from django.shortcuts import render_to_response, get_object_or_404

def listado(request):
    publicaciones = Post.objects.all()
    return render_to_response('publicaciones.html', {'publicaciones':publicaciones})

def detalle(request, idpost):
    post = Post.objects.get(pk=idpost)
    return render_to_response('detalle.html', {'post':post })

def galerias(request):
    galerias = Galeria.objects.all()
    return render_to_response('galerias.html', {'galerias':galerias})

def detallegaleria(request, idgaleria):
    galeria = Galeria.objects.get(pk=idgaleria)
    fotos = Foto.objects.filter(galeria=galeria)
    return render_to_response('galeria.html', {'galeria':galeria, 'fotos':fotos})

from forms import PostForm, ContactoForm
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
def contacto(request):
    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje desde nuestro blog'
            contenido = formulario.cleaned_data['mensaje']
            contenido += 'comunicarse a: '+ formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['laoska@guegue.net'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        formulario = ContactoForm()
    return render_to_response('contactoform.html', {'formulario':formulario}, context_instance=RequestContext(request))

def nuevo_post(request):
    if request.method == 'POST':
        formulario = PostForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = PostForm()
    return render_to_response('postform.html', {'formulario':formulario}, context_instance=RequestContext(request))
