# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Post.created'
        db.alter_column('blog_post', 'created', self.gf('django.db.models.fields.DateField')())


    def backwards(self, orm):
        
        # Changing field 'Post.created'
        db.alter_column('blog_post', 'created', self.gf('django.db.models.fields.DateTimeField')())


    models = {
        'blog.author': {
            'Meta': {'object_name': 'Author'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'blog.foto': {
            'Meta': {'object_name': 'Foto'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'galeria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Galeria']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'blog.galeria': {
            'Meta': {'object_name': 'Galeria'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'blog.post': {
            'Meta': {'object_name': 'Post'},
            'authors': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Author']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateField', [], {}),
            'galleries': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Galeria']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['blog']
