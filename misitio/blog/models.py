from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateField()
    authors = models.ForeignKey(Author)
    galleries = models.ManyToManyField(to='Galeria', blank=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('detalle', (), {'idpost': self.pk} )

class Galeria(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True)
    
    def __unicode__(self):
        return self.titulo

class Foto(models.Model):
    galeria = models.ForeignKey(Galeria)
    foto = models.ImageField(upload_to='imagenes')
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True)
    
    def __unicode__(self):
        return self.titulo
