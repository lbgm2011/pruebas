from django.contrib import admin
from blog.models import *

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ['authors']
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)
admin.site.register(Author)