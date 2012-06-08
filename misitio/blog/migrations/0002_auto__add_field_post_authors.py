# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Post.authors'
        db.add_column('blog_post', 'authors', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['blog.Author']), keep_default=False)

        # Removing M2M table for field authors on 'Post'
        db.delete_table('blog_post_authors')

        # Adding M2M table for field galleries on 'Post'
        db.create_table('blog_post_galleries', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['blog.post'], null=False)),
            ('galeria', models.ForeignKey(orm['blog.galeria'], null=False))
        ))
        db.create_unique('blog_post_galleries', ['post_id', 'galeria_id'])


    def backwards(self, orm):
        
        # Deleting field 'Post.authors'
        db.delete_column('blog_post', 'authors_id')

        # Adding M2M table for field authors on 'Post'
        db.create_table('blog_post_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['blog.post'], null=False)),
            ('author', models.ForeignKey(orm['blog.author'], null=False))
        ))
        db.create_unique('blog_post_authors', ['post_id', 'author_id'])

        # Removing M2M table for field galleries on 'Post'
        db.delete_table('blog_post_galleries')


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
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'galleries': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Galeria']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['blog']
