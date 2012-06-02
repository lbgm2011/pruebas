from django.conf.urls.defaults import patterns, include, url
urlpatterns = patterns('blog.views',
    #url('(?P<idpost>\d+)/$', 'detalle'),
    (r'^(?P<idgaleria>\d+)/$', 'galerias'),

)
