from django.conf.urls.defaults import patterns, include, url
urlpatterns = patterns('blog.views',
    url('^$', 'listado', name='inicio'),
    url(r'^galerias/$', 'galerias'),
    url(r'^noticia/(?P<idpost>\d+)/$', 'detalle', name='detalle' ),
    url(r'^galeria/(?P<idgaleria>\d+)/$', 'detallegaleria', name='detallegaleria' ),
)
