from django.contrib import admin
from blog.models import *

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Galeria)
admin.site.register(Foto)
