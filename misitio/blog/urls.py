from django.conf.urls.defaults import patterns, include, url
urlpatterns = patterns('blog.views',
    url('(?P<idpost>\d+)/$', 'detalle'),
)
