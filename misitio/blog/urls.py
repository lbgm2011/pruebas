from django.conf.urls.defaults import patterns, include, url
urlpatterns = patterns('blog.views',
    url( '^$', 'listado', name='news_list'),
    url(r'^noticia/(?P<idpost>\d+)/$', 'detalle', name='detalle' ),

#    url('^galerias/$', 'galerias')
)
