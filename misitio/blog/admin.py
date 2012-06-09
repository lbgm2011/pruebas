from django.contrib import admin
from blog.models import *

class FotoInline( admin.TabularInline ):
    model = Foto

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]

class GaleriaAdmin( admin.ModelAdmin):
    inlines = [FotoInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Foto)
